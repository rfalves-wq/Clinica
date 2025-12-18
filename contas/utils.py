import re

def validar_cpf(cpf):
    # remove tudo que não é número
    cpf = re.sub(r'\D', '', cpf)

    # deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # não pode ser sequência repetida
    if cpf == cpf[0] * 11:
        return False

    # cálculo do primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    # cálculo do segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{dig1}{dig2}"
