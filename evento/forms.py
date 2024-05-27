from django import forms
from .models import Evento
from turmas.models import Turma

class EventoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        turma_id = kwargs.pop('turma_id', None)  # Remove turma_id dos argumentos de palavras-chave, se presente
        super(EventoForm, self).__init__(*args, **kwargs)
        if turma_id:
            self.fields['turma'].queryset = Turma.objects.filter(pk=turma_id)  # Filtra as opções do campo turma pelo turma_id fornecido
            self.fields['turma'].initial = turma_id  # Define o valor inicial do campo turma como o turma_id

    turma = forms.ModelChoiceField(
        queryset=Turma.objects.all(),
        widget=forms.HiddenInput(), 
        #required=True
    )  # Define o campo de turma como um ModelChoiceField com um widget HiddenInput

    data = forms.DateTimeField(
        #label='Data do evento', 
        widget=forms.DateInput(attrs={'type': 'datetime-local'}), 
        #required=True
    )  # Define o campo de data como um DateTimeField com um widget DateInput personalizado para entrada de data e hora

    class Meta:

        model = Evento  # Define o modelo a ser utilizado pelo formulário
        fields = ['titulo', 'descricao', 'data', 'turma']  # Define os campos a serem exibidos no formulário