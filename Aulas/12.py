# Comandos Aula 19 - Dicionários

# Inicia-se com dict() ou "{}".
pessoas = {"Nome": "Icaro", "Sexo": "M", "Idade": 21}

print(f"O {pessoas["Nome"]} possui {pessoas['Idade']} anos.")
print(pessoas.keys()) # Chaves: nome que o valor recebe.
print(pessoas.values()) # Valor: os dados presente nas chaves.
print(pessoas.items()) # Itens: a junção das chaves e valores.
del pessoas["Sexo"]
pessoas["Nome"] = "Cesar"
pessoas["Peso"] = 71.5

for k in pessoas.keys(): # Exibe as chaves.
    print(k)

for v in pessoas.values(): # Exibe os valores presentes nas chaves.
    print(v)

for i in pessoas.items(): # Exibe todos os elementos.
    print(i)

brasil = []

estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "São Paulo", "Sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]["UF"])
print(brasil[1]["Sigla"])

estado_1 = dict()
brasil_ = list()

for c in range(0,3):
    estado_1["UF"] = str(input("Unidade Federativa: "))
    estado_1["Sigla"] = str(input("Sigla: "))
    brasil.append(estado_1.copy()) # Função parecida com o "[:]" referente as listas.(Cria uma cópia.)

for e in brasil_:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")
