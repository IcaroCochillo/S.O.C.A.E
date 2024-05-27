from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('usuarios.urls')),
    path('', include('contato.urls')),
    path('', include('evento.urls')),
    path('', include('materia.urls')),
    path('', include('material.urls')),
    path('', include('notificacao.urls')),
    path('', include('turmas.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403 = 'usuarios.views.handler403'
handler404 = 'usuarios.views.handler404'