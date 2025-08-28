# Mundo 3 - Exercício 109 - Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
# Resolvido sem auxílio.

from Meu_pacote import Moeda

Verde = "\033[32m"

print(f"{Verde}")

p = float(input("Digite o preço: R$"))

print(f"A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}")
print(f"O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, True)}")
print(f"Aumentando 10%, temos {Moeda.aumentar(p, 0.10, True)}")
print(f"Diminuindo 13%, temos {Moeda.diminuir(p, 0.13, True)}")
