# Comandos Aula 16 - Tuplas

# Inicia-se com o "()" ou automaticamente após adicionar mais de um elemento em uma variável.
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata frita") #Tuplas são imutáveis, ou seja, seus elementos não podem ser alterados.

print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:3])
print(lanche[-4:-2])
print(len(lanche)) # Exibe a quantidade de índices presentes na tupla.
print(sorted(lanche)) # Exibe em ordem alfabética.

for comida in lanche:
    print(f"Eu vou comer {comida}.")

for contador in range(0,len(lanche)):
    print(f"Eu vou comer {lanche[contador]}.")

for contador in range(0,len(lanche)):
    print(f"Eu vou comer {lanche[contador]} na posição {contador}.")

for comida in enumerate(lanche):
    print(f"Eu vou comer {comida}.")


for posição, comida in enumerate(lanche):
    print(f"Eu vou  comer {comida} na posição {posição}.")

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
c2 = b + a

print(c)
print(c2)
print(c.count(5)) # Exibe a quantidade de vezes que elemento está presente.
print(c.index(8)) # Exibe o índice onde ocorre a primera ocorência do elemento.

pessoa = ("Icaro", 21, "M", 71.5) # A tupla pode armazenar diferentes tipos de dados.

print(pessoa)
del(pessoa) # Deleta os dados da tupla.
