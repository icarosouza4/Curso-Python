# Mundo 3 - Exercício 108 - Adapte o cógido do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
# Resolvido sem auxílio.

from Meu_pacote import Moeda

Vermelho = "\033[31m"

print(f"{Vermelho}")

p = float(input("Digite o preço: R$"))

print(f"Analisando o valor de {Moeda.moeda(p)}, concluimos que:")
print(f"A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}")
print(f"O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}")
print(f"Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(p, 0.10))}")
print(f"Diminuindo 13%, temos {Moeda.moeda(Moeda.diminuir(p, 0.13))}")
