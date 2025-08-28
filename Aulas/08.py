# Comandos Aula 13 - Estruturas de repetição(for)

for contagem in range(0,10): # Laço de repetição.(Contagem de 1 a 10.)
    print(contagem + 1) # Utiliza-se o "+1" pois a contagem começa no "0" com a ausência dele.

for contagem in range(10,0,-1): # Laço de repetição.(Contagem de 10 a 1.(Utiliza-se o "-1" para contar de trás para frente)) 
    print(contagem)

for contagem in range(0,20,2): # Laço de repetiçao, definindo o passo como "2", ou seja, uma contagem pulando de 2 em 2.
    print(contagem)

soma = 0

for c in range(0,5): # Laço de repetição com o alcance de 5 repetições.
    n = int(input("Digite um número inteiro: ")) # Variável "n" que armazena um número inteiro.
    soma += n # Variável "soma" que recebe o valor de "n" e armazena-o de maneira somatória.
    
print("A soma de todos os valores digitados foi {}.".format(soma)) # Resultado da soma dos cinco valores digitados.
