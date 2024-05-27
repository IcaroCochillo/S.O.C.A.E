from django.db import models

# Create your models here.
class Turma(models.Model):
    ano = models.IntegerField(verbose_name="Ano", help_text="Digite o ano da turma")
    nome_turma = models.CharField(max_length=100, verbose_name="Nome", help_text="Digite o nome da turma")

    def __str__(self):
        return str(self.nome_turma)
    
    class Meta: 
        verbose_name = 'Turma' 
        verbose_name_plural = 'Turmas' 