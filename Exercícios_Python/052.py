# Mundo 2 - Exercício 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Resolvido sem auxílio.

num = int(input("Digite um número: "))

total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\33[4;31m", end="")
        total += 1
    else:
        print("\33[33m", end="")
    print("{}".format(c), end=" ")
    print("\33[m", end="")
    
if total == 2:
    print("\nO número {} é primo.".format(num))
    print("Ele foi divisível {} vezes.".format(total))
else:
    print("\nO número {} não é primo.".format(num))
    print("Ele foi divisível {} vezes.".format(total))
