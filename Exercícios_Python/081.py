# Mundo 3 - Exercício 081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# Resolvido sem auxílio.

Azul = "\033[34m"

print(f"{Azul}")

listanumeros = []

while True:
    listanumeros.append(int(input("Digite um número: ")))
    resposta = str(input("Deseja continuar? [S/N] ").strip().upper())
    if resposta == "N":
        break

listanumeros.sort(reverse=True)

print(f"Foram digitados {len(listanumeros)} números.")
print(f"A lista em ordem decrescente fica {listanumeros}.")

if 5 in listanumeros:
    print("O número 5 está presente na lista.")
else:
    print("O número 5 não está presente na lista.")
