# Mundo 3 - Exercício 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
# Resolvido sem auxílio.

from random import randint
from time import sleep

Amarelo = "\033[33m"

print(f"{Amarelo}")

def sorteio(lista):
    print(f"Sorteando 5 valores da lista:", end = " ")
    
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n}", end = " ")
        sleep(0.3)
    print("PRONTO!")

def par(lista):
    soma = 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares da {lista}, temos {soma}.")

numeros = list()
sorteio(numeros)
par(numeros)
