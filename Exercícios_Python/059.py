# Mundo 2 - Exercício 059 - Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")

opcao = int(input("Digite a opção desejada: "))

while opcao != 5:
    if opcao == 1:
        print(f"A soma entre {n1} e {n2} é igual a {n1 + n2}.")
    elif opcao == 2:
        print(f"A multiplicação entre {n1} e {n2} é igual a {n1 * n2}.")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número é {n1}.")
        else:
            print(f"O maior número é {n2}.")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida, tente novamente.")
    opcao = int(input("Digite a opção desejada: "))
