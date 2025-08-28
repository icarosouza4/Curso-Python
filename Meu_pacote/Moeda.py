def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco * (1 + taxa)
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco * (1 - taxa)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato is False else moeda(res) 


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, taxa1 = 10, taxa2 = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preco, taxa1/100, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preco, taxa2/100, True)}')
    print('-' * 30)

