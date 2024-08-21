from django.shortcuts import render, redirect
from .forms import UsuarioCreationForm, UsuarioChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import Aluno
from django.contrib import messages

def registration(request):
    form = UsuarioCreationForm()

    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada, faça login")
            return redirect('login')
    
    return render(request, 'registration/registration.html', {'registration' : True, 'form': form})

@login_required
def perfil(request):
    user = Aluno.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil alterado")
            return redirect('perfil')
        else:
            messages.error(request, "ERRO")
            return redirect('perfil')
    elif request.method == 'GET':
        form = UsuarioChangeForm(instance=user)
        return render(request, 'registration/perfil.html', {'user': user, 'form': form})

@login_required
def liderinativos(request):
    if request.method == 'POST':
        usuarios_ativar = request.POST.getlist('usuarios_ativar')
        Aluno.objects.filter(pk__in=usuarios_ativar).update(is_active=True)
        return redirect('liderInativos')
    elif request.method == 'GET':
        usuarios_inativos = Aluno.objects.filter(is_active=False)
        return render(request, 'registration/usuarios_inativos.html', {'usuarios_inativos': usuarios_inativos})

class MyLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('listar-eventos')
        return super().dispatch(request, *args, **kwargs)

def sair(request):
    logout(request)
    return redirect('login')


# templates de erros:
def handler403(request, exception):
    return render(request, 'error/403.html')

def handler404(request, exception):
    return render(request, 'error/404.html')
