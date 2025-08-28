def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(",",".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO! \'{entrada}\' é um preço inválido!\033[m")
        else:
            válido = True
            return float(entrada)

        
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

        
def leiaFloat(numero):
    while True:
        try:
            n = float(input(numero))
        except (ValueError, TypeError):
            print("\033[31mERRO!Digite um número real.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mProgama interrompido.\033[m")
            return 0
        else:
            return n 
            
