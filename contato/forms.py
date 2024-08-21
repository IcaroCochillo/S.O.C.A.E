from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato  # Define o modelo a ser utilizado pelo formulário
        fields = ['nome', 'telefone', 'email', 'horario_atend']  # Define os campos a serem exibidos no formulário