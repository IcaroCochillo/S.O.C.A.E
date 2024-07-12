from rolepermissions.roles import AbstractUserRole

# Definição da classe de papel de usuário para Aluno
class Aluno(AbstractUserRole):
    # Definindo permissões para o Aluno
    available_permissions = {
        'visualizarContatoProfessor': True,
        'visualizarEventos': True,
        'visualizarMateriais': True,
        'visualizarMaterias': True,
        'visualizarTurmas': True,
        'visualizarNotificacoes': True,
    }

class Lider(AbstractUserRole):
    # Definindo permissões para o Lider
    available_permissions = {
        'visualizarContatoProfessor': True,
        'adicionarContatoProfessor': True, 
        'editarContatoProfessor': True, 
        'excluirContatoProfessor': True, 

        'visualizarEventos': True,
        'adicionarEvento': True,
        'editarEvento': True,
        'excluirEvento': True,
        
        'visualizarMateriais': True,
        'adicionarMateria': True,
        'editarMateria': True,
        'excluirMateria': True,

        'visualizarMaterias': True,
        'adicionarMateria': True,
        'editarMateria': True,
        'excluirMateria': True,

        'visualizarTurmas': True,
        'adicionarTurma': True, 
        'editarTurma': True, 
        'excluirTurma': True, 

        'visualizarNotificacoes': True,
        'adicionarNotificacao': True, 
        'editarNotificacao': True, 
        'excluirNotificacao': True, 
    }