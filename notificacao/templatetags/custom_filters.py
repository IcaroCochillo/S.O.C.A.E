from django import template
from notificacao.utils import contar_notificacoes_nao_lidas, notificacoes
register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": field.field.widget.attrs.get('class', '') + ' ' + css_class})

@register.simple_tag
def notificacoes_nao_lidas(usuario):
    return contar_notificacoes_nao_lidas(usuario)

@register.simple_tag
def todas_notificacoes(usuario):
    return notificacoes(usuario)