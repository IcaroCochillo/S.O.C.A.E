from django.contrib import admin
from .models import Contatoprofessor

@admin.register(Contatoprofessor)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'telefone', 'email', 'horario_atend', 'nome')