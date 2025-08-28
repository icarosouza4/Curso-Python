# Mundo 1 - Exercício 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é {num2}.")
else:
    print(f"O maior número é {num3}.")

if num1 < num2 and num1 < num3:
    print(f"O menor número é {num1}.")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é {num2}.")
else:
    print(f"O menor número é {num3}.")
