# Mundo 3 - Exercício 092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Resolvido sem auxílio.

from datetime import datetime

Magenta = "\033[35m"

print(f"{Magenta}")

dados = {}

dados["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados["Idade"] = datetime.now().year - nasc
dados["CTPS"] = int(input("Carteira de Trabalho (0 se não possui): "))

if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35)) - datetime.now().year

print("-="*30)

for k,v in dados.items():
    print(f"-> {k} tem o valor {v}.")

print("-="*30)
