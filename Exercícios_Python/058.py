# Mundo 2 - Exercício 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# Resolvido sem auxílio.

from random import randint

Vermelho = "\033[31m"

print(f"{Vermelho}")

computador = randint(0,10)
jogador = ""
tentativas = 0

print("""O computador está pensando em um número entre 0 e 10.
Tente adivinhar qual é o número.""")

while jogador != computador:
    jogador = int(input("Digite um número: "))
    if jogador == computador:
        print("Você acertou!")
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        else:
            print("Menos... Tente mais uma vez.")
    tentativas += 1

print(f"Você acertou o número em {tentativas} tentativas.")
print("Fim do jogo!")
