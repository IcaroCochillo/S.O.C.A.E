from django.shortcuts import redirect, render, get_object_or_404
from .models import Contato
from .forms import ContatoForm
from rolepermissions.decorators import has_permission_decorator  # Importa o decorador de permissão
from django.contrib import messages  # Importa o módulo de mensagens do Django

# has_permission_decorator é um Decorador para verificar permissões

# Views para manipular contatos de professores

# View para listar todos os contatos de professores
@has_permission_decorator('visualizarContato')
def listar(request):
    if request.method == 'GET':        
        contatos = Contato.objects.all()  # Obtém todos os contatos de professores do banco de dados
        formContato = ContatoForm()  # Instancia o formulário para criar novos contatos

        context = {
            'contatos': contatos,  # Passa os contatos para o contexto
            'formContato': formContato,  # Passa o formulário para o contexto
        }
        return render(request, 'contatos/list.html', context)  # Renderiza a página HTML com os contatos e o formulário

# View para criar um novo contato de professor
@has_permission_decorator('adicionarContato')
def criar(request):
    if request.method == 'POST':  # Verifica se a solicitação é POST
        form = ContatoForm(request.POST)  # Instancia o formulário com os dados da solicitação
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo contato no banco de dados
            messages.success(request, "Contato criado com sucesso")  # Exibe mensagem de sucesso
            return redirect('listar-contatos')  # Redireciona para a página de listagem de contatos
        else:
            messages.error(request, "ERRO")
            return redirect('listar-contatos')
        
# View para editar um contato de professor existente
@has_permission_decorator('editarContato')
def editar(request, contato_id):
    if request.method == 'POST':  # Verifica se a solicitação é POST
        contato = Contato.objects.get(pk=contato_id)  # Obtém o contato pelo ID
        form = ContatoForm(request.POST, instance=contato)  # Instancia o formulário com os dados da solicitação e o contato existente
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações do contato no banco de dados
            messages.success(request, "Contato editado com sucesso")
            return redirect('listar-contatos')
        else:
            messages.error(request, "ERRO")
            return redirect('listar-contatos')

# View para excluir um contato de professor existente
@has_permission_decorator('excluirContato')
def excluir(request, contato_id):
    if get_object_or_404(Contato, pk=contato_id):  
        contato = get_object_or_404(Contato, pk=contato_id)# Obtém o contato pelo ID ou retorna 404 se não encontrado
        contato.delete()  # Exclui o contato do banco de dados
        messages.success(request, "Contato excluido com sucesso")
        return redirect('listar-contatos') 
    else:
            messages.error(request, "ERRO")
            return redirect('listar-contatos')