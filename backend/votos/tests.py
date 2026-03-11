from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Usuario, Enquete, Opcao, Voto


class VotosViewsTests(TestCase):
    def setUp(self):
        # create normal user and admin
        self.user = Usuario.objects.create_user(email="user@example.com", nome="Utilizador", senha="pass123")
        self.admin = Usuario.objects.create_superuser(email="admin@example.com", nome="Admin", senha="pass123")

        # enquete activa com duas opções
        agora = timezone.now()
        self.enquete = Enquete.objects.create(
            usuario=self.admin,
            titulo="Enquete de Teste",
            descricao="Descrição",
            dataInicio=agora - timezone.timedelta(hours=1),
            dataFim=agora + timezone.timedelta(hours=1),
            status='ativa',
        )
        self.opcao1 = Opcao.objects.create(enquete=self.enquete, descricao="Opção 1")
        self.opcao2 = Opcao.objects.create(enquete=self.enquete, descricao="Opção 2")

    def test_detail_requires_login(self):
        url = reverse('detalhe_enquete', args=[self.enquete.pk])
        response = self.client.get(url)
        # login URL is /entrar/ as configured in settings
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

    def test_vote_and_results(self):
        self.client.login(email=self.user.email, password="pass123")
        url = reverse('detalhe_enquete', args=[self.enquete.pk])

        # GET should render form
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submeter Voto")

        # submit vote
        response = self.client.post(url, {'opcao': self.opcao1.pk}, follow=True)
        self.assertContains(response, "Voto registado com sucesso")

        # the option should have incremented
        self.opcao1.refresh_from_db()
        self.assertEqual(self.opcao1.quantidadeVotos, 1)

        # results section should appear
        self.assertContains(response, "Resultados")
        self.assertContains(response, "Opção 1")

    def test_admin_cannot_vote(self):
        self.client.login(email=self.admin.email, password="pass123")
        url = reverse('detalhe_enquete', args=[self.enquete.pk])
        response = self.client.post(url, {'opcao': self.opcao1.pk}, follow=True)
        self.assertContains(response, "Administradores não podem votar")

