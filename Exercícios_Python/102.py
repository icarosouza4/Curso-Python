# Mundo 3 - Exercício 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
# Resolvido com auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

def fatorial(n,show = False):
    """
    Cálculo de fatorial.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar a conta completa.
    :return: Retornar o valor do fatorial.
    """
    f = 1
    
    for c in range(n,0,-1):
        if show:
            print(c, end = "")
            if c > 1:
                print(" x ", end = "")
            else:
                print(" = ", end = "")
        f *= c
    return f


help(fatorial)
print("*-="*20)
num = int(input("Digite um número para ver o seu fatorial: "))
print("-="*20)
print(fatorial(num,show=True))
print("-="*20)
