from .models import Notificacao

def contar_notificacoes_nao_lidas(usuario):
    return Notificacao.objects.filter(usuario=usuario, lida=False).count()

def notificacoes(usuario):
    return Notificacao.objects.filter(usuario=usuario)