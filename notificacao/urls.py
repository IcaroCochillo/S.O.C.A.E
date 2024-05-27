from django.urls import path
from . import views

urlpatterns = [
    path('notificacoes/', views.listar, name='listar-notificacoes'),
    path('notificacao/criar/', views.criar, name='criar-notificacao'),
    path('notificacao/editar/', views.editar, name='editar-notificacao'),
    path('notificacao/excluir/', views.excluir, name='excluir-notificacao'),

    path('lernotificacao/<int:notificacao_id>/', views.lernotificacao, name='lernotificacao'),
    path('excluirnotificacao/', views.excluirnotificacao, name='excluirnotificacao'),
]