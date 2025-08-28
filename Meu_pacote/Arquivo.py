from Meu_pacote import Interface

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um \033[31mERRO\033[0m na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("\033[31mERRO\033[0m ao ler arquivo!")
    else:
        Interface.cabeçalho("Pessoas cadastradas")
        for linha in a:
            dados = linha.split(";")
            dados[1] = dados[1].replace("\n","")
            print(f"{dados[0]:<30}{dados[1]:>4} anos")
    finally:
        a.close()


def cadastrar(arquivo, nome = "Desconhecido", idade = 0):
    try:
        a = open(arquivo, "at")
    except:
        print("Houve um \033[31mERRO\033[0m na criação do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um \033[31mERRO\033[0m na hora de escrever os dados!")
        else:
            print(f"{nome} foi registrado com sucesso!")
            a.close()

