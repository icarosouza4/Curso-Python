# Mundo 2 - Exercício 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

s = 0

for num in range(1,7):
    num = int(input("Digite o {} valor: ".format(num)))
    if num % 2 == 0:
        s += num

print("A soma dos números pares é igual a {}.".format(s))
