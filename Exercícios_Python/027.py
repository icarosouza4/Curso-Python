# Mundo 1 - Exercício 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Resolvido sem auxílio.

Azul = "\033[34m"

print(f"{Azul}")

nome = str(input("Digite o nome completo: ")).strip()

print(f"O nome completo é: {nome}.")
print(f"O primeiro nome é: {nome.split()[0]}.")
print(f"O último nome é: {nome.split()[-1]}.")
