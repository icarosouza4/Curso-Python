# Mundo 1 - Exercício 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# Resolvido sem auxílio.

from random import choice

Verde = "\033[32m"

print(f"{Verde}")

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

print(f"O aluno escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}.")
