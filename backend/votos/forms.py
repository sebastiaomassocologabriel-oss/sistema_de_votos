from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Enquete, Opcao
from django.utils import timezone

class RegistoForm(UserCreationForm):
    nome = forms.CharField(max_length=100, label="Nome Completo")
    
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("nome", "email", "tipo")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Se não for admin logado, o tipo padrão é eleitor e o campo fica oculto
        if not user or not user.is_authenticated or user.tipo != 'admin':
            self.fields.pop('tipo')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True}))

class EnqueteForm(forms.ModelForm):
    opcoes_texto = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Uma opção por linha (mínimo 2)'}),
        label="Opções",
        help_text="Insira as opções da enquete, uma por linha."
    )

    class Meta:
        model = Enquete
        fields = ['titulo', 'descricao', 'dataInicio', 'dataFim', 'status']
        widgets = {
            'dataInicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dataFim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        dataInicio = cleaned_data.get("dataInicio")
        dataFim = cleaned_data.get("dataFim")
        opcoes_texto = cleaned_data.get("opcoes_texto")

        if dataInicio and dataFim and dataInicio >= dataFim:
            raise forms.ValidationError("A data de início deve ser anterior à data de fim.")
        
        # if dataInicio and dataInicio < timezone.now():
        #      raise forms.ValidationError("A data de início não pode ser no passado.")

        if opcoes_texto:
            opcoes = [o.strip() for o in opcoes_texto.split('\n') if o.strip()]
            if len(opcoes) < 2:
                raise forms.ValidationError("A enquete deve ter pelo menos 2 opções.")
            cleaned_data['opcoes_lista'] = opcoes
        
        return cleaned_data
