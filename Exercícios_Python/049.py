# Mundo 2 - Exercício 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

num = int(input("Digite um número para ver sua tabuada: "))

for c in range(1, 11):
    print(f"{num} x {c} = {num * c}")
