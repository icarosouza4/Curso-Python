# Comandos Aula 9 - Manipulando textos

frase = "Curso em Vídeo Python"

frase[9] # Lê o dado no índice "9".(O índice começa no "0".)
frase[9:13] # Lê os dados do índice "9" ao índice "13".(O dado do índice "13" não é lido)
frase[9:21] # Lê os dados do índice "9" ao índice "21", ou seja, do "9" até o final.
frase[9:21:2] # Lê os dados do índice "9" ao índice "21", saltando de 2 em 2 índices.
frase[:5] # Lê os dados do índice "0" ao índice "5".
frase[15:] # Lê os dados do índice "15" até o último índice.
frase[9::3] # Lê os dados do índice "9" até o último índice, saltando de 3 em 3 índices.

len(frase) # Exibe a quantidade de índices.
frase.count("o") # Conta a quatidade de vezes que a letra "o" está presente.
frase.count("o", 0, 13) # Conta a quatidade de vezes que a letra "o" está presente, do início até o índice "13".
frase.find("deo") # Encontra o índice onde se inicia o elemento.
frase.find("Android") # Retorna o valor "-1", pois o elemento não foi encontrado.

"Curso" in frase # Verifica se o elemento "Curso" está presente na variável "frase". Retornando o valor True ou False.

frase.replace("Python","Android") # Substitui um elemento pela outro. Neste caso, "Python" por "Android".
frase.upper() # Transforma o elemento em maiúsculo.
frase.lower() # Transforma o elemento em minúsculo.
frase.capitalize() # Formata a primeira letra do elemento em maiúsculo, e transforma o restante em minúsculo.
frase.title() # Formata a primeira letra de cada palavra do elemento para maísculo.(Onde houver espaços, haverá uma quebra de palavras)
frase.strip() # Remove tanto os espaços do início, quanto do final do elemento.
frase.rstrip() # Remove somente os espaços da direita, ou seja, do final do elemento.
frase.lstrip() # Remove somente os espaços da esquerda, ou seja, do início do elemento.

frase.split() # Divide o elemento baseado nos espaços presentes nele, gerando uma lista
"-".join(frase) # Gera um elemento único, baseado na lista, separando-a por "-".(Como se fosse uma junção.)
