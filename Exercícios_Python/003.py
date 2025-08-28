# Mundo 1 - Exercício 003 - Crie um programa que leia dois números e mostre a soma entre eles.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"
Branco_brilhante = "\033[97m"

n1 = int(input(f"{Branco_brilhante}Digite o primeiro número: "))
n2 = int(input(f"{Branco_brilhante}Digite o segundo número: "))

s = n1 + n2

print("{}A soma entre {} e {} é igual a {}.".format(Magenta_brilhante, n1, n2, s))
