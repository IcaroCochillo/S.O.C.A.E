from django.urls import path
from . import views

urlpatterns = [
    path('materiais/<int:materia_id>/', views.listar, name='listar-materiais'),
    path('material/criar/', views.criar, name='criar-material'),
    path('material/editar/<int:material_id>/', views.editar, name='editar-material'),
    path('material/excluir/<int:material_id>/', views.excluir, name='excluir-material'),
]