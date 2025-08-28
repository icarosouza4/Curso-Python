def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print("\033[31mERRO!Digite um número inteiro.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mPrograma interrompido.\033[m")
            return 0
        else:
            return n
        

def linha(tamanho = 42):
    return "-" * tamanho


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho("Sistema de cadastro")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\33[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opção = leiaInt("\033[32mSua opção: \033[m")
    return opção 
    
