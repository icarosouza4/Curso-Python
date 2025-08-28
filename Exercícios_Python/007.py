# Mundo 1 - Exercício 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média entre {nota1} e {nota2} é igual a {media}.")
