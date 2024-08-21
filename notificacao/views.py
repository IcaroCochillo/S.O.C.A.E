from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from alunos.models import Aluno
from .models import Notificacao
from .forms import NotificacaoForm
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('visualizarNotificacoes')
def listar(request):
    if request.method == 'GET':      
        turma = request.user.turma
        notificacoes = Notificacao.objects.filter(usuario__turma=turma).values('titulo', 'assunto').distinct()

        formNotificacao = NotificacaoForm()

        context = {
            'notificacoes': notificacoes,
            'formNotificacao': formNotificacao,
        }
        return render(request, 'notificacoes/list.html', context)

@has_permission_decorator('adicionarNotificacao')
def criar(request):
    if request.method == 'POST':
        form = NotificacaoForm(request.POST)
        if form.is_valid():
            notificacao_data = form.cleaned_data
            turma = request.user.turma
            alunos = Aluno.objects.filter(turma=turma)
            
            for aluno in alunos:
                Notificacao.objects.create(
                    usuario=aluno,
                    titulo=notificacao_data['titulo'],
                    assunto=notificacao_data['assunto']
                )
                
            messages.success(request, "Notificações criadas com sucesso")
            return redirect('listar-notificacoes')
        else:
            messages.error(request, "Erro ao criar notificações")
            return redirect('criar-notificacao')
    
    form = NotificacaoForm()
    return render(request, 'notificacoes/criar.html', {'form': form})

@has_permission_decorator('editarNotificacao')
def editar(request):
    if request.method == 'POST':
        form = NotificacaoForm(request.POST)
        print(form)

        if form.is_valid():
            titulo_antigo = form.cleaned_data['titulo_antigo']
            novo_titulo = form.cleaned_data['titulo']
            novo_assunto = form.cleaned_data['assunto']
            
            # Filtrar as notificações com base no título antigo
            notificacoes_antigas = Notificacao.objects.filter(titulo=titulo_antigo)
            
            # Atualizar todas as notificações filtradas com os novos detalhes
            for notificacao in notificacoes_antigas:
                notificacao.titulo = novo_titulo
                notificacao.assunto = novo_assunto
                notificacao.save()

            messages.success(request, "Material editada com sucesso")
            return redirect('listar-notificacoes')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-notificacoes')

@has_permission_decorator('excluirNotificacao')
def excluir(request):
    if request.method == 'POST':
        notificacaotitulo = request.POST.get('notificacaotitulo')
        if Notificacao.objects.filter(titulo=notificacaotitulo):
            notificacoes = Notificacao.objects.filter(titulo=notificacaotitulo)
            notificacoes.delete()
            messages.success(request, "Material excluida com sucesso")
            return redirect('listar-notificacoes')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-notificacoes')    


@login_required
def lernotificacao(request, notificacao_id):
    usuario = request.user
    notificacao = get_object_or_404(Notificacao, pk=notificacao_id, usuario=usuario)
    notificacao.lida = True
    notificacao.save()
    
    url_anterior = request.META.get('HTTP_REFERER', None)
    if url_anterior:
        return HttpResponseRedirect(url_anterior)
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def excluirnotificacao(request):
    todas = request.GET.get("todas")
    if todas == "sim":
        notificacao = Notificacao.objects.filter(usuario=request.user)
    elif todas == "nao":
        notificacao = Notificacao.objects.filter(usuario=request.user, lida=True)
    if notificacao:
        notificacao.delete()
   
    url_anterior = request.META.get('HTTP_REFERER', None)
    if url_anterior:
        return HttpResponseRedirect(url_anterior)
    else:
        return HttpResponseRedirect(reverse('home'))