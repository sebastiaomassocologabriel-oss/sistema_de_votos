from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None, tipo='eleitor'):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, tipo=tipo)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha=None):
        user = self.create_user(email, nome, senha, tipo='admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPOS = (
        ('admin', 'Administrador'),
        ('eleitor', 'Eleitor'),
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  # voltar para 100
    tipo = models.CharField(max_length=20, choices=TIPOS, default='eleitor')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

class Enquete(models.Model):
    STATUS_CHOICES = (
        ('ativa', 'Ativa'),
        ('encerrada', 'Encerrada'),
        ('pendente', 'Pendente'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enquetes')
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    dataInicio = models.DateTimeField()
    dataFim = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def is_active(self):
        agora = timezone.now()
        return self.status == 'ativa' and self.dataInicio <= agora <= self.dataFim

    @property
    def total_votos(self):
        return self.voto_set.count()

    def __str__(self):
        return self.titulo

class Opcao(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, related_name='opcoes')
    descricao = models.CharField(max_length=30)
    quantidadeVotos = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao

class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
    dataVoto = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'enquete')

    def __str__(self):
        return f"Voto de {self.usuario.nome} em {self.enquete.titulo}"
