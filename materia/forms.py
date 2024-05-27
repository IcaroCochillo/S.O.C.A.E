from django import forms
from .models import Materia
from turmas.models import Turma

class MateriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        turma_id = kwargs.pop('turma_id', None)
        super(MateriaForm, self).__init__(*args, **kwargs)
        if turma_id:
            self.fields['turma'].queryset = Turma.objects.filter(pk=turma_id)
            self.fields['turma'].initial = turma_id

    turma = forms.ModelChoiceField(
        queryset=Turma.objects.all(),
        widget=forms.HiddenInput(), 
        required=True
    )

    class Meta:
        model = Materia
        fields = ['nome_materia', 'professor', 'turma']