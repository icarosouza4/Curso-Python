# Mundo 3 - Exercício 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
# Resolvido sem auxílio.

from Meu_pacote import Moeda

Preto = "\033[30m"

print(f"{Preto}")

p = float(input("Digite o preço: R$"))

print(f"Analisando o valor de R${p}, concluimos que:")
print(f"A metade de R${p} é R${Moeda.metade(p)}")
print(f"O dobro de R${p} é R${Moeda.dobro(p)}")
print(f"Aumentando 10%, temos R${Moeda.aumentar(p, 0.10)}")
print(f"Diminuindo 13%, temos R${Moeda.diminuir(p, 0.13)}")
