# Mundo 2 - Exercício 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

print("Cadastro de pessoas.")
maior = 0
homem = 0
mulher = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F] ").upper()
    if idade > 18:
        maior += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher += 1
    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

print(f"\nAo todo temos {maior} pessoas maiores de 18 anos.")
print(f"Ao todo temos {homem} homens cadastrados.")
print(f"Ao todo temos {mulher} mulheres com menos de 20 anos.")
