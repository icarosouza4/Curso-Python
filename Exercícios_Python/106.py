# Mundo 3 - Exercício 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# Resolvido sem auxílio.

from time import sleep

c = ("\033[m",         # 0 - Sem cores
     "\033[0;30;41m",  # 1 - Vermelho
     "\033[0;30;42m",  # 2 - Verde
     "\033[0;30;43m",  # 3 - Amarelo
     "\033[0;30;44m",  # 4 - Azul
     "\033[0;30;105m", # 5 - Roxo
     "\033[7;97m"      # 6 - Branco
     )


def ajuda(com):
    título(f"Acessando o manual do comando \" {com}\"", 3)
    print(c[1], end = "")
    help(com)
    print(c[0], end = "")
    sleep(2)


def título(msg, cor = 0):
    tam = len(msg) + 4

    print(c[cor], end = "")
    print("-=" * tam)
    print(f"  {msg}")
    print("-=" * tam)
    print(c[0], end = "")
    sleep(1)


comando = ""

while True:
    título("Sistema de ajuda PyHelp", 4)
    comando = str(input("Função ou Biblioteca -> "))
    
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
        
título("Até logo!", 3)
