# Mundo 2 - Exercício 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência de Fibonacci.
# Resolvido sem auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

print("Sequência de Fibonacci.")
num = int(input("Digite um número para ver sua sequência de Fibonacci: "))
t1 = 0
t2 = 1

while num > 0:
    print(f"{t1} - {t2}", end=" ")
    t1 = t2
    t2 = t1 + t2
    num -= 1
