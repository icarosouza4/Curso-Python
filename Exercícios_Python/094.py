# Mundo 3 - Exercício 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas cadastradas.
# B) A média da idade.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.
# Resolvido sem auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

pessoa = {}
listagem = []
soma = média = 0

while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("Sexo inválido. Tente novamente.")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    listagem.append(pessoa.copy())
    while True:
        resp = str(input("Deseja continuar? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("Resposta inválida. Tente novamente.")
    if resp == "N":
        break

print("-="*30)
print(f"A todo foram cadastradas {len(listagem)} pessoas.")

média = soma/len(listagem)

print(f"A média de idade é {média:.2f}.")
print("As mulheres cadastradas foram: ", end = "")

for p in listagem:
    if p["Sexo"] in "F":
        print(f"{p["Nome"]} ", end = "")

print()
print("Lista das pessoas acima da média de idade: ")

for p in listagem:
    if p["Idade"] >= média:
        print("     ", end = "")
        for k,v in p.items():
            print(f"{k} = {v};", end = "")
        print()

print("< FIM >")
print("-="*30)
