from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Aluno
from rolepermissions.roles import assign_role

class UsuarioCreationForm(UserCreationForm):
    # Campos adicionais no formulário de criação de usuário
    data_nasc = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta(UserCreationForm.Meta):
        model = Aluno
        fields = ('nome', 'email', 'matricula', 'data_nasc', 'turma', 'lider', 'password1', 'password2')
    
    # Validação personalizada para o campo 'matricula'
    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if Aluno.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Esta matrícula já está em uso. Por favor, escolha outra.")
        return matricula
    
    # Validação personalizada para o campo 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Aluno.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso. Por favor, escolha outro.")
        return email

    # Sobrescrevendo o método save() para atribuir permissões de acordo com o tipo de usuário
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        # Atribuindo o papel de 'lider' ou 'aluno' de acordo com a escolha no formulário
        if user.lider:
            user.is_active = False
            assign_role(user, 'lider')
        else:
            assign_role(user, 'aluno')
        
        if commit:
            user.save()
        
        return user
    
class UsuarioChangeForm(UserChangeForm):
    # Campo adicional no formulário de alteração de usuário
    data_nasc = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta(UserChangeForm.Meta):
        model = Aluno
        fields = ('nome', 'email', 'matricula', 'data_nasc', 'turma', 'lider')

    # Validação personalizada para o campo 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica se o email foi alterado e se já está em uso por outro usuário
        if 'email' in self.changed_data and Aluno.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email já está em uso. Por favor, escolha outro.")
        return email

    # Sobrescrevendo o método save() para atribuir permissões de acordo com o tipo de usuário
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Verificar o estado anterior do campo 'lider'
        was_lider = Aluno.objects.get(pk=user.pk).lider

        # Se o usuário foi marcado como líder no formulário e não era líder antes
        if user.lider and not was_lider:
            user.is_active = False
            assign_role(user, 'lider')
        else:
            assign_role(user, 'aluno')
        
        if commit:
            user.save()
        
        return user
    
    # Personalizando a inicialização do formulário para definir o valor inicial do campo 'data_nasc'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removendo o campo de senha do formulário de alteração de usuário
        self.fields.pop('password')
        # Definindo o valor inicial do campo 'data_nasc' se estiver disponível no objeto do usuário
        if self.instance.pk:
            data_nascimento = self.instance.data_nasc
            if data_nascimento:
                self.initial['data_nasc'] = data_nascimento.strftime('%Y-%m-%d')
