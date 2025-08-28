# Comandos Aula 10 - Condições(Parte 1)

tempo = int(input("Quantos anos tem seu carro? "))

if tempo <= 3: # Condição(Se o tempo for igual ou menor que 3, executa o bloco True, se não, executa o bloco False.)
    print("Seu carro é novo!") # Bloco True
else:
    print("Seu carro é velho...") # Bloco False

print("-- Fim --")

print("Carro novo." if tempo <= 3 else "Carro velho.") # Condição simplificada.

# Comandos Aula 12 - Condições(Parte 2)

nome = str(input("Digite seu nome: "))

if nome == "Icaro": # Condição normal True
    print("É o meu nome!")
elif nome == "João" or nome == "Maria" or nome == "Gabriel" or nome == "Ana": # Condição alinhada True
    print("Seu nome é bem popular no Brasil.")
elif nome in "Yasmin Isabela Rosa": # Condição alinhada True
    print("Belo nome feminino!")
else: # Condição normal False
    print("Seu nome é comum.")

print("Tenha um bom dia, {}!".format(nome))
