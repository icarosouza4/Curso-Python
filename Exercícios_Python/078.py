# Mundo 3 - Exercício 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# Resolvido sem auxílio.

Vermelho = "\033[31m"

print(f"{Vermelho}")

lista = []
maior = 0
menor = 0

for cont in range(0,5):
    lista.append(int(input(f"Digite um valor para a {cont+1}º posição: ")))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

posicoes_maior = []
for i in range(len(lista)):
    if lista[i] == maior:
        posicoes_maior.append(i + 1)


posicoes_menor = []
for i in range(len(lista)):
    if lista[i] == menor:
        posicoes_menor.append(i + 1)

print(f"Você digitou os valores {lista}.")
print(f"O maior valor digitado foi {maior} e ele se encontra nas posições {posicoes_maior}.")
print(f"O menor valor digitado foi {menor} e ele se encontra nas posições {posicoes_menor}.")
