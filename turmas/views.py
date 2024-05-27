from django.shortcuts import redirect, render, get_object_or_404
from .models import Turma
from .forms import TurmaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages

@has_permission_decorator('visualizarTurmas')
def listar(request):
    if request.method == 'GET':        
        turmas = Turma.objects.all()
        formTurma = TurmaForm()

        context = {
            'turmas': turmas,
            'formTurma': formTurma,
        }
        return render(request, 'turmas/list.html',context)

@has_permission_decorator('adicionarTurma')
def criar(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Turma criada com sucesso")
            return redirect('listar-turma')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-turma')

@has_permission_decorator('editarTurma')
def editar(request, turma_id):
    if request.method == 'POST':
        turma = Turma.objects.get(pk=turma_id)
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            messages.success(request, "Turma editada com sucesso")
            return redirect('listar-turma')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-turma')

@has_permission_decorator('excluirTurma')
def excluir(request, turma_id):
    if get_object_or_404(Turma, pk=turma_id):
        turma = get_object_or_404(Turma, pk=turma_id)
        turma.delete()
        messages.success(request, "Turma excluida com sucesso")
        return redirect('listar-turma')
    else:
        messages.error(request, "ERRO")
        return redirect('listar-turma')