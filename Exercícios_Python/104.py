# Mundo 3 - Exercício 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Resolvido com auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um NÚMERO inteiro válido. \033[m")
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
