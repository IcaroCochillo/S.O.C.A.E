from django.urls import path
from . import views

urlpatterns = [
    path('turmas/', views.listar, name='listar-turma'),
    path('turma/criar/', views.criar, name='criar-turma'),
    path('turma/editar/<int:turma_id>/', views.editar, name='editar-turma'),
    path('turma/excluir/<int:turma_id>/', views.excluir, name='excluir-turma'),
]