# Comandos Aula 17 - Listas(Parte 1)

# Inicia-se com list[] ou "[]".
num = [2, 5, 9, 1]

num[2] = 3 # Muda o elemento presente no índice para o novo.
num.append(7) # Adiciona um elemento a lista.
num.sort() # Exibe a lista em ordem crescente.
num.sort(reverse= True) # Exibe a lista em ordem decrescente.
num.insert(2, 2) # Adiciona um elemento no índice.
num.pop(2) # Elimina o elemento presente no índice.
num.remove[2] # Remove o elemento indicado da lista.(Na sua primeira ocorrência.)

print(num)
print(f"Essa lista em {len(num)} elementos.")

if 5 in num:
    num.remove(5)
else:
    print("O número 5 não está presente na lista.")

valores = list()
valores2 = list()

valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f"{v}...")

for c, v in enumerate(valores):
    print(f"Na posição {c}, encontrei o valor {v}!")

for contagem in range(0,5):
    valores2.append(int(input("Digite um número inteiro: ")))

print(valores)
print(valores2)

a = [2, 3, 4, 7]
b = a # Faz uma ligação entre as listas, ou seja, caso uma seja alterada, a outra também será alterada.
b = a[:] # Cria uma cópia da lista A e armazena na lista B.(É uma forma de copiar os dados de uma lista, sem alterar a lista original.)
b[2] = 8

print(f"Lista A: {a}.")
print(f"Lista B: {b}.")

# Comandos Aula 18 - Listas(Parte 2)

teste = list()

teste.append("Icaro")
teste.append(21)

galera = list()

galera.append(teste[:])
teste[0] = "Yan"
teste[1] = 24
galera.append(teste[:])

print(galera)

galera2 = [["Icaro",21], ["Yan",24], ["Yasmin",20], ["Isabela",2]]

print(galera2[0])
print(galera2[0][0])

for p in galera2:
    print(f"O {p[0]} possui {p[1]} anos.")

galera3 = list()
dados = list()

for c in range(0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera3.append(dados[:])
    dados.clear()

print(galera3)

totalmaior = totalmenor = 0

for p in galera3:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade.")
        totalmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totalmenor += 1

print(f"Temos {totalmaior} pessoas maiores de idade e {totalmenor} menores de idade.")
    