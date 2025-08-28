# Mundo 2 - Exercício 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
# Resolvido sem auxílio.

Preto = "\033[30m"

print(f"{Preto}")

sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

while sexo not in ["M", "F"]:
    sexo = str(input("Dados inválidos. Por favor, digite novamente: ")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso.")
