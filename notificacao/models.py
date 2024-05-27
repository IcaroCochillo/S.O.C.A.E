from django.db import models
from usuarios.models import Aluno

# Create your models here.
class Notificacao(models.Model):
    usuario = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, verbose_name="Título", help_text="Digite o título da notificação")
    assunto = models.TextField(verbose_name="Assunto", help_text="Digite o assunto da notificação")
    lida = models.BooleanField(default=False)

    def __str__(self):
        return self.assunto
    
    class Meta: 
        verbose_name = 'Notificação' 
        verbose_name_plural = 'Notificações' 