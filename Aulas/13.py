# Comandos Aula 20 - Funções(Parte 1)

# def: inicia a função. "Nome da função". "()" parâmetro da função.
from calendar import c
from re import A


def lin():
    print("-" * 20)


lin() # Chama a função.
print("CURSO EM VÍDEO")
lin()

def título(texto): # O "texto" é o parâmetro da função.
    print("-" * 20)
    print(texto.upper())
    print("-" * 20)


título("Curso de Python") # O "Curso de Python" vai ser passado como parâmetro da função.

def soma(n1,n2):
    print(f"N1 = {n1} e N2 = {n2}")

    soma = n1 + n2

    print(f"A soma {n1} + {n2} é igual a {soma}.")


soma(5, 5)
soma(n2= 10,n1 = 15) # Existe a possibilidade de declarar o parâmetro de maneira que a ordem é alterada.

def contador(* n): # Desempacota os parâmetros.(É a possibilidade de passar um parâmetro sem uma quantidade já predefinida pela própia função.)
    tam = len(n)

    print(f"Informei os valores {n} e são ao todo {tam} números.")


contador(5, 7, 1, 2, 6, 9, 2, 1, 2)

def dobra(lista):
    pos = 0

    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [5, 7, 1, 2, 3, 2, 9]

dobra(valores)
print(valores)

# Comandos Aula 21 - Funções(Parte 2)

# help() #Ajuda interativa do próprio Python.(Exibe um manual.)
# print(input.__doc__)

def contador2(i, f, p):
    """
    A função contador2 faz uma contagem, onde o início, o fim e o passo são definidos pelo usuário.
    :param i: Define o início da contagem.
    :param f: Define o fim da contagem.
    :param p: Define o passo da contagem.
    :return: Sem retorno.
    Função criada por Icaro, com o auxílio das aulas de Gustavo Guanabara do Curso Em Vídeo.
    """
    c = i

    while c <= f:
        print(f"{c}", end = "...")
        c += p

    print("Fim...")


contador2(2, 10, 2)
help(contador2)

def somar(n1 = 0, n2 = 0, n3 = 0): # É possível declarar parâmetros como opcionais. Basta dar um valor a eles na função.
    """
    A função somar realiza a soma dos valores definidos pelo usuário.
    :param n1: Define o primeiro valor.
    :param n2: Define o segundo valor.
    :param n3: Define o terceiro valor.
    :return: Sem retorno.
    Função criada por Icaro, com o auxílio das aulas de Gustavo Guanabara do Curso Em Vídeo.
    """
    s = n1 + n2 + n3

    print(f"A soma vale {s}.")


somar(4, 9, 1)
somar(n2 = 10, n1 = 17)

def teste():
    X = 20 # A variável "X" possui escopo local, ou seja, ela só irá existir dentro da função.

    print(f"Na função teste, N vale {N}.")
    print(f"Na função teste, X vale {X}.")


N = 10 # A variável "N" possui escopo global, ou seja, ela está presente em todo o programa.

print(f"No programa principal, N vale {N}.")
teste()

def função():
    n1 = 5

    print(f"N1 dentro vale {n1}.") # N1 dentro da função vale 5.


n1 = 10

função()
print(f"N1 fora vale {n1}.") # N1 fora da função vale 10.
# É possível ter duas variáveis de mesmo nome, no entanto, elas ficam separadas por escopo. 
# Existe no caso, uma variável N1 dentro da função e uma outra variável N1 fora da função.

def teste2(b):
    global a # Este comando torna a variável "a" em escopo global.

    a = 8
    b += 4
    c = 2

    print(f"'A' dentro vale {a}.")
    print(f"'B' dentro vale {b}.")
    print(f"'C' dento vale {c}.")


a = 5

teste2(a)
print(f"'A' fora vale {a}.")

def somar2(n1 = 0, n2 = 0, n3 = 0):
    s = n1 + n2 + n3
    
    return s # Função utilizada para encerrar a execução da função e devolver um valor ao local onde a função foi chamada.


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f"Os resultados foram: {r1}, {r2} e {r3}.")

def fatorial(num = 1):
    f = 1

    for cont in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))

print(f"O fatorial de {n} é igual a {fatorial(n)}.")

f1 = fatorial(10)
f2 = fatorial(5)
f3 = fatorial(3)

print(f"Os resultados foram: {f1}, {f2} e {f3}.")

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))

if par(num):
    print(f"O {num} é par.")
else:
    print(f"O {num} não é par.")
