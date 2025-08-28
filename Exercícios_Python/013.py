# Mundo 1 - Exercício 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Resolvido sem auxílio.

Preto = "\033[30m"

print(f"{Preto}")

salario = float(input("Digite o salário do funcionário:R$ "))

aumento = salario * 0.15
salario_com_aumento = salario + aumento

print(f"O salário do funcionário com aumento de 15% é de R${salario_com_aumento:.2f}.")
