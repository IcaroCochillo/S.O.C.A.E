from django.urls import path
from . import views

urlpatterns = [
    path('materias/', views.listar, name='listar-materias'),
    path('materia/criar/', views.criar, name='criar-materia'),
    path('materia/editar/<int:materia_id>/', views.editar, name='editar-materia'),
    path('materia/excluir/<int:materia_id>/', views.excluir, name='excluir-materia'),
]