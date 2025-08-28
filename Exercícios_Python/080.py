# Mundo 3 - Exercício 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# Resolvido com auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

numeros = []

for c in range(0,5):
    num = (int(input(f"Digite o um valor: ")))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
        print("Número adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                print(f"Número adicionado na posiçao {pos} da lista.")
                break
            pos += 1
            
print(f"Em ordem, os valores digitados foram {numeros}.")
