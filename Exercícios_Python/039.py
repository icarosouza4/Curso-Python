# Mundo 2 - Exercício 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# A) Se ele ainda vai se alistar ao serviço militar.
# B) Se é a hora de se alistar.
# C) Se já passou do tempo do alistamento.
# D) Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Resolvido com auxílio.

from datetime import date

Verde = "\033[32m"

print(f"{Verde}")

ano_atual = date.today().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

print("Qual é o seu sexo?")
print("[ 1 ] Masculino")
print("[ 2 ] Feminino")

sexo = int(input("Digite sua opção: "))

if sexo == 1:
    if idade < 18:
        print(f"Você ainda não precisa se alistar.")
    elif idade == 18:
        print(f"Você tem {idade} anos. Está na hora de se alistar.")
    else:
        print(f"Você já passou do prazo para se alistar.")
        print(f"Você deveria ter se alistado há {idade - 18} anos.") 
else:
    print("Você não precisa se alistar.")
