from django.db import models

# Create your models here.
class Materia(models.Model):
    nome_materia = models.CharField(max_length=100, verbose_name="Nome", help_text="Digite o nome da materia")
    professor = models.ForeignKey("contato.Contato", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Professor", help_text="Selecione o professor da materia")
    turma = models.ForeignKey("turmas.Turma", on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return str(self.nome_materia)
    
    class Meta: 
        verbose_name = 'Matéria' 
        verbose_name_plural = 'Matérias' 