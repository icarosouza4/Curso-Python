# Mundo 3 - Exercício 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

pessoa = []
dados = []
ppesado = []
pleve = []
mpesado = mleve = None

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoa.append(dados[:])
    if mpesado is None or dados[1] > mpesado:
        mpesado = dados[1]
    if mleve is None or dados[1] < mleve:
        mleve = dados[1]
    if dados[1] >= 80:
        ppesado.append(dados[:])
    if dados[1] < 60:
        pleve.append(dados[:])
    dados.clear()
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if r == "N":
        break

print("="*45)
print(f"No total, foram cadastradas {len(pessoa)} pessoas.")
print("="*45)
print(f"As pessoas consideradas pesadas foram:")

for p in ppesado:
    print(f"{p[0]} pesando {p[1]}Kg.")

print("="*45)
print(f"As pessoas consideradas leves foram:")

for pp in pleve:
    print(f"{pp[0]} pesando {pp[1]}Kg.")
    
print("="*45)
print(f"O maior peso registrado foi {mpesado}Kg.")
print(f"O menor peso registrado foi {mleve}Kg.")
print("="*45)
