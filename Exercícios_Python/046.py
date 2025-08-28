# Mundo 2 - Exercício 046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# Resolvido sem auxílio.

from time import sleep

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

for c in range(10, -1, -1):
    print(c)
    sleep(1)
    
print("\033[31mBOOM!\033[0m")
