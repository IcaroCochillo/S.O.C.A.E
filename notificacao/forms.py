from django import forms
from .models import Notificacao

class NotificacaoForm(forms.ModelForm):
    titulo_antigo = forms.CharField(widget=forms.HiddenInput())  # Campo oculto para armazenar o título antigo

    class Meta:
        model = Notificacao
        fields = ['titulo', 'assunto']