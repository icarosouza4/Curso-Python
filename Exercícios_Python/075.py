# Mundo 3 - Exercício 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: quantas vezes apareceu o valor 9; em que posição foi digitado o primeiro valor 3; quais foram os números pares.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

num = (int(input("Digite o 1ª número: ")),int(input("Digite o 2ª número: ")),
       int(input("Digite o 3ª número: ")),int(input("Digite o 4ª número: ")))

print(f"Você digitou os seguintes números: {num}")
print(f"O número 9 apareceu {num.count(9)} vez(es).")

if 3 in num:
    print(f"O número 3 apareceu na {num.index(3)+1}ª posição.")
else:
    print("Não há o número 3 na escolha de números.")

print("Os valores pares digitados foram: ", end="")

for n in num:
    if n % 2 == 0:
        print(n, end=" ")
