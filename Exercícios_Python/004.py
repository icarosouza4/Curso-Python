# Mundo 1 - Exercício 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Resolvido com auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

tipo = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(tipo)}.")
print(f"Só tem espaços? {tipo.isspace()}.") #
print(f"É um número? {tipo.isnumeric()}.")
print(f"É alfabético? {tipo.isalpha()}.")
print(f"É alfanumérico? {tipo.isalnum()}.")
print(f"Está em maiúsculas? {tipo.isupper()}.")
print(f"Está em minúsculas? {tipo.islower()}.")
print(f"Está capitalizada? {tipo.istitle()}.")
