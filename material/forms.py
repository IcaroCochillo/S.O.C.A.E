from django import forms
from .models import Material
from materia.models import Materia

class MaterialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        materia_id = kwargs.pop('materia_id', None)
        super(MaterialForm, self).__init__(*args, **kwargs)
        if materia_id:
            self.fields['materia'].queryset = Materia.objects.filter(pk=materia_id)
            self.fields['materia'].initial = materia_id

    materia = forms.ModelChoiceField(
        queryset=Materia.objects.all(),
        widget=forms.HiddenInput(), 
        required=True
    )

    class Meta:
        model = Material
        fields = ['titulo', 'arquivo', 'descricao', 'materia']