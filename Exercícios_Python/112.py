# Mundo 3 - Exercício 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chama leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
# Resolvido com auxílio.

from Meu_pacote import Dados, Moeda

Magenta = "\033[35m"

print(f"{Magenta}")

p = Dados.leiaDinheiro("Digite o preço: R$")

Moeda.resumo(p, 35, 22)
