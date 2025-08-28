# Mundo 3 - Exercício 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicinário com as seguintes informações:
# A) Quantidade de notas.
# B) A maior nota.
# C) A menor nota.
# D) A média da turma.
# E) A situação (opcional).
# F) Adicione docstrings.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

def notas(*n, sit = False):
    """
    Análise de notas.
    :param n: As notas.
    :param sit: (Opcional) A situação.
    :return: Dicionário com as notas e situação.
    """
    r = dict()
    r["Total"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Média"] = sum(n)/len(n)
    
    if sit:
        if r["Média"] >= 7:
            r["Situação"] = "Boa"
        elif r["Média"] >= 5:
            r["Situação"] = "Razoável"
        else:
            r["Situação"] = "Ruim"
    return r


help(notas)
resp = notas(2.5,10.0,8.0, sit = True)
print(resp)
