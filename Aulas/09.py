# Comandos Aula 14 - Estruturas de repetição(while)

c = 0

while c < 10: # Contagem de 1 a 10 utilizando while.
    print(c + 1)
    c += 1
    
print("-- Fim --")

n = None
par = ímpar = 0

while n != 0: # Enquanto o número for diferente de "0", repete o laço infinitamente.
    n = int(input("Digite um número inteiro: "))
    if n != 0:
        if n % 2 == 0: # Se o resto da divisão por 2 for igual a 0, armazena o número na variável par, se não, armazena-se na ímpar.
            par += 1 # Contagem de números pares.
        else:
            ímpar += 1 # Contagem de números ímpares.

print("Forma digitados {} números pares e {} números ímpares.".format(par,ímpar)) # Resultado final.

resposta = "S"

while resposta == "S": # Laço de repetição onde o usuário decide quando encerrar utilizando uma variável "resposta".
    n = int(input("Digite um número inteiro: "))
    resposta = str(input("Deseja continuar? [S / N] ")).upper().strip()

print("-- Fim --")

#Comandos Aula 15 - Estruturas de repetição(Interrompendo while)

n = s = 0

while True: # Repetição infinita
    n = int(input("Digite um número inteiro: ")) # Entrada de dados.(número)
    if n == 999: # Condição para quebra de repetição.
        break # Quebra de repetição.
    s += n # Variável que soma os números de forma cumulativa.

print(f"A soma de todos os números vale {s}.") # Resultado final da soma.
