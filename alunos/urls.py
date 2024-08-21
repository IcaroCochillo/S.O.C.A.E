# enquetes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.sair, name="logout"),
    path("registration/", views.registration, name="registration"),
    path("perfil/", views.perfil, name="perfil"),
    path("liderInativos/", views.liderinativos, name="liderInativos"),
]
