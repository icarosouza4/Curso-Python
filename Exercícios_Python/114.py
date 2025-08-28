# Mundo 3 - Exercício 114 - Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
# Resolvido com auxílio.

import urllib
import urllib.request

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except:
    print("O site não está acessível no momento.")
else:
    print("O site está acessível no momento.")
