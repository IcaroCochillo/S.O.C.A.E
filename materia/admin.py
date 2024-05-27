from django.contrib import admin
from .models import Materia
# Register your models here.

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_materia')