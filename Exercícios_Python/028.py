# Mundo 1 - Exercício 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Resolvido sem auxílio.

from random import randint

Magenta_brilhante = "\033[95m"

print(f"{{Magenta_brilhante}}")

numero_pensado = randint(0, 5)

print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
numero_usuario = int(input("Em que número eu pensei? "))

if numero_usuario == numero_pensado:
    print("Parabéns! Você acertou!")
else:
    print(f"Ganhei! Eu pensei no número {numero_pensado} e não no número {numero_usuario}!")
