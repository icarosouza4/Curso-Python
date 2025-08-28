# Mundo 2 - Exercício 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

n = 0
soma = 0
cont = 0
maior = float("-inf")
menor = float("inf")

print("Vamos ler vários números e calcular a soma, o maior, o menor e a média entre eles.")

while True:
    n = float(input("Digite um número: "))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta != "S":
        break

media = soma / cont

print(f"\nAnalisando todos os números informados, conclui-se que:")
print(f"A soma é igual a {int(soma)}.")
print(f"A média é igual a {media:.1f}.")
print(f"O maior número digitado foi {int(maior)}.")
print(f"O menor número digitado foi {int(menor)}.")
