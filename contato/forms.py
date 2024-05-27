from django import forms
from .models import Contatoprofessor

class ContatoprofessorForm(forms.ModelForm):
    class Meta:
        model = Contatoprofessor  # Define o modelo a ser utilizado pelo formulário
        fields = ['nome', 'telefone', 'email', 'horario_atend']  # Define os campos a serem exibidos no formulário