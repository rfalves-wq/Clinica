from django import template
import re

register = template.Library()

@register.filter
def mascara_cpf(valor):
    if not valor:
        return ''
    cpf = re.sub(r'\D', '', valor)
    if len(cpf) != 11:
        return valor
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
