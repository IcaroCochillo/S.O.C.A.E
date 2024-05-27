from django.shortcuts import redirect, render, get_object_or_404
from .models import Material
from .forms import MaterialForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages

@has_permission_decorator('visualizarMaterias')
def listar(request, materia_id):
    if request.method == 'GET':        
        materiais = Material.objects.filter(materia=materia_id)
        formMaterial = MaterialForm(materia_id=materia_id)

        context = {
            'materiais': materiais,
            'formMaterial': formMaterial,
        }
        return render(request, 'materiais/list.html', context)

@has_permission_decorator('adicionarMateria')
def criar(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            materia_id = form.cleaned_data['materia']
            form.save()
            messages.success(request, "Material criada com sucesso")
            return redirect('listar-materiais', materia_id=materia_id.id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar-materiais', materia_id=materia_id.id)

@has_permission_decorator('editarMateria')
def editar(request, material_id):
    if request.method == 'POST':
        material = Material.objects.get(pk=material_id)
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            materia_id = form.cleaned_data['materia']
            form.save()
            messages.success(request, "Material editada com sucesso")
            return redirect('listar-materiais', materia_id=materia_id.id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar-materiais', materia_id=materia_id.id)

@has_permission_decorator('excluirMateria')
def excluir(request, material_id):
    if get_object_or_404(Material, pk=material_id):
        material = get_object_or_404(Material, pk=material_id)
        materia_id = material.materia.id
        material.delete()
        messages.success(request, "Material excluida com sucesso")
        return redirect('listar-materiais', materia_id=materia_id)
    else:
        messages.error(request, "ERRO")
        return redirect('listar-materiais', materia_id=materia_id.id)
