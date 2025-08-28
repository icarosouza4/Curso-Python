# Mundo 3 - Exercício 086 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

matriz2 = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz2[l][c] = int(input(f"Digite um valor para {l},{c}: "))
        
print("="*30)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz2[l][c]:^5}]", end="")
    print()
    
print("="*30)
