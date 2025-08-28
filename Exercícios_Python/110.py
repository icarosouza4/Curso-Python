# Mundo 3 - Exercício 110 - Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
# Resolvido sem auxílio.

from Meu_pacote import Moeda

Amarelo = "\033[33m"

print(f"{Amarelo}")

p = float(input("Digite o preço: R$"))

Moeda.resumo(p, 20, 15)
