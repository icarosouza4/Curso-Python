# Mundo 3 - Exercício 082 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

listanumeros = []
listapares = []
listaimpar = []

while True:
    numero = int(input("Digite um número inteiro: "))
    listanumeros.append(numero)
    if numero % 2 == 0:
        listapares.append(numero)
    else:
        listaimpar.append(numero)
    print("Número adicionado a lista.")
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == "N":
        break

print(f"Os número informados foram: {listanumeros}.")
print(f"Sendo os pares: {listapares}.")
print(f"E os ímpares: {listaimpar}.")
