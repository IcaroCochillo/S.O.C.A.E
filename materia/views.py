from django.shortcuts import redirect, render, get_object_or_404
from .models import Materia
from .forms import MateriaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages

# Create your views here.
@has_permission_decorator('visualizarMateriais')
def listar(request):
    if request.method == 'GET': 
        try:
            turma_id= request.user.turma.id
        except:
            messages.error(request, 'Você não tem nenhuma turma, vá em Perfil e escolha sua turma. Caso sua truma não esteja listada converse com o Líder')
            return redirect('listar-turma')
        materias = Materia.objects.filter(turma=turma_id)
        formMateria = MateriaForm(turma_id=turma_id)

        context = {
            'materias': materias,
            'formMateria': formMateria,
        }
        return render(request, 'materias/list.html',context)

@has_permission_decorator('adicionarMateria')
def criar(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia criada com sucesso")
            return redirect('listar-materias')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-materias')
        
@has_permission_decorator('editarMateria')
def editar(request, materia_id):
    if request.method == 'POST':
        materia = Materia.objects.get(pk=materia_id)
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia editada com sucesso")
            return redirect('listar-materias')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-materias')

@has_permission_decorator('excluirMateria')
def excluir(request, materia_id):
    if get_object_or_404(Materia, pk=materia_id):
        materia = get_object_or_404(Materia, pk=materia_id)
        materia.delete()
        messages.success(request, "Materia excluida com sucesso")
        return redirect('listar-materias')
    else:
        messages.error(request, "ERRO")
        return redirect('listar-materias')