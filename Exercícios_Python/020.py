# Mundo 1 - Exercício 020 - O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# Resolvido sem auxílio.

from random import shuffle

Ciano = "\033[36m"

print(f"{Ciano}")

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print(f"A ordem de apresentação será: {", ".join(lista)}.")
