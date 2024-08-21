from django.shortcuts import redirect, render, get_object_or_404

from notificacao.models import Notificacao
from alunos.models import Aluno
from .models import Evento
from .forms import EventoForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages

@has_permission_decorator('visualizarEventos')
def listar(request):
    try:
        turma_id = request.user.turma.id
    except AttributeError:
        messages.error(request, 'Você não tem nenhuma turma. Por favor, vá em Perfil e escolha sua turma. Se sua turma não estiver listada, converse com o Líder.')
        return redirect('listar-turma')

    eventos = Evento.objects.filter(turma=turma_id)
    formEvento = EventoForm(turma_id=turma_id)

    context = {
        'eventos': eventos,
        'formEvento': formEvento,
    }
    return render(request, 'eventos/list.html', context)

@has_permission_decorator('adicionarEvento')
def criar(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            turma = evento.turma
            alunos = Aluno.objects.filter(turma=turma)
            data_formatada = evento.data.strftime('%d/%m/%Y %H:%M')
            for aluno in alunos:
                Notificacao.objects.create(
                    usuario=aluno,
                    titulo=evento.titulo,
                    assunto=f"{evento.descricao} - {data_formatada}"
                )

            messages.success(request, "Evento criado com sucesso")
            return redirect('listar-eventos')
        else:
            messages.error(request, "Erro ao criar evento")
            return redirect('listar-eventos')

    # Se não for uma requisição POST, renderize o formulário vazio
    form = EventoForm()
    return render(request, 'seu_template.html', {'form': form})

@has_permission_decorator('editarEvento')
def editar(request, evento_id):
    if request.method == 'POST':
        evento = Evento.objects.get(pk=evento_id)
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            messages.success(request, "Evento editado com sucesso")
            form.save()
            return redirect('listar-eventos')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-eventos')

@has_permission_decorator('excluirEvento')
def excluir(request, evento_id):
    if get_object_or_404(Evento, pk=evento_id):  
        evento = get_object_or_404(Evento, pk=evento_id)
        evento.delete()
        messages.success(request, "Evento excluido com sucesso")
        return redirect('listar-eventos')
    else:
        messages.error(request, "ERRO")
        return redirect('listar-eventos')