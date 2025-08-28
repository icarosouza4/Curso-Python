# Mundo 2 - Exercício 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# A) Média abaixo de 5.0: REPROVADO.
# B) Média entre 5.0 e 6.9: RECUPERAÇÃO.
# C) Média 7.0 ou superior: APROVADO.
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Sua média é {media:.1f}")

if media < 5.0:
    print("Você está reprovado.")
elif media >= 5.0 and media < 6.9:
    print("Você está de recuperação.")
else:
    print("Você está aprovado.")
