from django.db import models

# Create your models here.
class Material(models.Model):
    descricao = models.TextField(verbose_name="Descrição", help_text="Digite a descrição do material")
    arquivo = models.FileField(upload_to='materiais/', blank=True, null=True, verbose_name="Arquivo", help_text="Selecione um arquivo")
    titulo = models.CharField(max_length=100, verbose_name="Título", help_text="Digite o título do material")
    materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)
    
    class Meta: 
        verbose_name = 'Material' 
        verbose_name_plural = 'Materiais' 