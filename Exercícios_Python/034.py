# Mundo 1 - Exercício 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    print(f"O salário do funcionário é R$ {salario * 1.1:.2f}. Pois ele recebeu um aumento de 10%.")
else:
    print(f"O salário do funcionário é R$ {salario * 1.15:.2f}. Pois ele recebeu um aumento de 15%.")
