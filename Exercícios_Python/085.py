# Mundo 3 - Exercício 085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em  uma lista única que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

listanum = [[],[]]

for c in range(0,7):
    num = int(input(f"Digite o {c+1}º número: "))
    if num % 2 == 0:
        listanum[0].append(num)
    else:
        listanum[1].append(num)

listanum[0].sort()
listanum[1].sort()

print(f"Os valores pares digitados foram: {listanum[0]} ")
print(f"Os valores ímpares digitados foram: {listanum[1]}")
