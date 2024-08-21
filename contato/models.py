from django.db import models

class Contato(models.Model):
    telefone = models.CharField(max_length=20, verbose_name="Telefone", help_text="Digite o telefone do professor")
    email = models.EmailField(verbose_name="Email", help_text="Digite o email do professor")
    horario_atend = models.CharField(max_length=100, verbose_name="Horário de Atendimento", help_text="Digite o horário de atendimento do professor")
    nome = models.CharField(max_length=100, verbose_name="Nome", help_text="Digite o nome do professor")

    def __str__(self):
        return str(self.nome)
    
    class Meta: 
        verbose_name = 'Contato' 
        verbose_name_plural = 'Contatos' 