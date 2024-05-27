from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título", help_text="Digite o título do evento")
    descricao = models.TextField(verbose_name="Descrição", help_text="Digite a descrição do evento")
    data = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Data do envento", help_text="Digite a data do evento")
    turma = models.ForeignKey("turmas.Turma", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)
    
    class Meta: 
        verbose_name = 'Evento' 
        verbose_name_plural = 'Eventos' 