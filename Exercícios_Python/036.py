# Mundo 2 - Exercício 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Quanto você ganha por mês? R$ "))
anos = int(input("Em quantos anos você pretende pagar? "))

prestacao = casa / (anos * 12)

if prestacao > salario * 0.3:
    print("Empréstimo negado.")
    print(f"O valor da prestação é de R$ {prestacao:.2f} e excede 30% do seu salário.")	
else:
    print("Empréstimo aprovado.")
    print(f"Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de R$ {prestacao:.2f}.")
