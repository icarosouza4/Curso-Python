# Mundo 1 - Exercício 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
# Resolvido sem auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

num = int(input("Digite um número: "))

snum = num + 1
anum = num - 1

print("O sucessor de {} é {} e o antecessor é {}.".format(num, snum, anum))
