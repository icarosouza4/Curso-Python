# Mundo 2 - Exercício 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos: MIRIM; até 14 anos: INFANTIL; até 19 anos: JUNIOR; até 25 anos: SÊNIOR; acima: MASTER.
# Resolvido sem auxílio.

from datetime import date

Azul = "\033[34m"

print(f"{Azul}")

nascimento = int(input("Digite o ano de nascimento do atleta: "))

ano = date.today().year
idade = ano - nascimento

print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Classificação: Mirim")
elif idade <= 14:
    print("Classificação: Infantil")
elif idade <= 19:
    print("Classificação: Junior")
elif idade <= 25:
    print("Classificação: Sênior")
else:
    print("Classificação: Master")
