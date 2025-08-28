# Mundo 3 - Exercício 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

numeros = []

while True:
    valores = int(input("Digite um valor: "))
    if valores not in numeros:
        numeros.append(valores)
        print("Valor adicionado.")
    else:
        print("Valor duplicado, não será adcionado.")
    resposta = str(input("Deseja adicionar outro valor? [S/N]").strip().upper())
    if resposta == "N":
        break

numeros.sort

print(f"Os números adicionados foram {numeros}.")
