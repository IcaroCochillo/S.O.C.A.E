from django.urls import path
from . import views  # Importa as views do aplicativo

# Define as URLs do aplicativo de contatos
urlpatterns = [
    # URL para listar todos os contatos de professores
    path('contatos/', views.listar, name='listar-contatos'),  
    # URL para criar um novo contato de professor
    path('contato/criar/', views.criar, name='criar-contato'),  
    # URL para editar um contato de professor existente, onde <int:contato_id> é substituído pelo ID do contato
    path('contato/editar/<int:contato_id>/', views.editar, name='editar-contato'),  
    # URL para excluir um contato de professor existente, onde <int:contato_id> é substituído pelo ID do contato
    path('contato/excluir/<int:contato_id>/', views.excluir, name='excluir-contato'),  
]
