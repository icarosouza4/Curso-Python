# Mundo 2 - Exercício 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque (10% de desconto); à vista no cartão (5% de desconto); em até 2x no cartão (preço normal); 3x ou mais no cartão (20% de juros).
# Resolvido sem auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

preco = float(input("Digite o preço do produto: R$ "))

print("Selecione a forma de pagamento:")
print("[1] à vista dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] em até 2x no cartão")
print("[4] 3x ou mais no cartão")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco * 1.2
    parcelas = int(input("Digite o número de parcelas: "))
    print(f"Sua compra será parcelada em {parcelas}x de R$ {total / parcelas:.2f} com juros.")
else:
    print("Opção inválida. Tente novamente.")

print(f"O total a pagar é R${total:.2f}.")
