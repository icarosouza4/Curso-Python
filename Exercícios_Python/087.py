# Mundo 3 - Exercício 087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor segunda linha.
# Resolvido com auxílio.

Preto = "\033[30m"

print(f"{Preto}")

matriz2 = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somacoluna3 = maior2linha = 0

for l in range(0,3):
    for c in range(0,3):
        matriz2[l][c] = int(input(f"Digite um valor para {l},{c}: "))
        
print("="*30)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz2[l][c]:^5}]", end="")
        if matriz2[l][c] % 2 == 0:
            somapar += matriz2[l][c]

    print()

print("="*30)
print(f"A soma dos valores pares é: {somapar}.")

for l in range(0,3):
    somacoluna3 += matriz2[l][2]

print(f"A soma dos valores da terceira coluna é:{somacoluna3}.")

for c in range(0,3):
    if c == 0:
        maior2linha = matriz2[1][c]
    elif matriz2[1][c] > maior2linha:
        maior2linha = matriz2[1][c]

print(f"O maior valor da segunda linha é: {maior2linha}.")
print("="*30)
