# Mundo 3 - Exercício 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

numext = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    numusu = int(input("Digite um número de 0 a 20: "))
    if 0 <= numusu <= 20:
        break
    print("Tente outro número. ", end="")

print(f"Você digitou o número {numusu}. Que por extenso, se escreve {numext[numusu]}.")
