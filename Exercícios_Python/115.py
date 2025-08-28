# Mundo 3 - Exercício 115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
# Resolvido com auxílio.

from Meu_pacote import Arquivo,Dados,Interface
from time import sleep

arquivo = "Pessoas_cadastradas.txt"

if not Arquivo.arquivoExiste(arquivo):
    Arquivo.criarArquivo(arquivo)

while True:
    resposta = Interface.menu(["Exibir pessoas cadastradas","Cadastrar uma nova pessoa","Sair do sistema"])
    if resposta == 1:
        Interface.cabeçalho("Pessoas cadastradas")
    elif resposta == 2:
        Interface.cabeçalho("Cadastre uma nova pessoa")
        nome = str(input("Digite o nome: "))
        idade = Interface.leiaInt("Idade: ")
        Arquivo.cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        Interface.cabeçalho("Encerrando o programa...")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
