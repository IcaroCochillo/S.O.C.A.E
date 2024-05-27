from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .base import AlunoManager

class Aluno(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, verbose_name="Nome", help_text="Informe o nome")
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Informe o email")
    data_nasc = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento", help_text="Informe a data de nascimento")
    matricula = models.CharField(max_length=14, unique=True, verbose_name="Matrícula", help_text="Informe a matrícula")
    lider = models.BooleanField(default=False, verbose_name="Líder", help_text="Marque esta caixa se for líder. OBS: Sujeito a aceitação")
    turma = models.ForeignKey("turmas.Turma", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Turma", help_text="Selecione a sua turma")

    # Define campos adicionais para permissões de usuário
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Define o campo de usuário para login como matrícula
    USERNAME_FIELD = "matricula"
    # Define os campos obrigatórios para criar um usuário (necessário para o comando createsuperuser)
    REQUIRED_FIELDS = ['nome', 'email']
    # Define o gerenciador de objetos personalizado para o modelo Aluno
    objects = AlunoManager()

    def __str__(self):
        return str(self.nome)
    
    class Meta: 
        verbose_name = 'Aluno' 
        verbose_name_plural = 'Alunos' 