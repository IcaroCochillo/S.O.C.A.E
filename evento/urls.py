from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.listar, name='listar-eventos'),
    path('evento/criar/', views.criar, name='criar-evento'),
    path('evento/editar/<int:evento_id>/', views.editar, name='editar-evento'),
    path('evento/excluir/<int:evento_id>/', views.excluir, name='excluir-evento'),
]