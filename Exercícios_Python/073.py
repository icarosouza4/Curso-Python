# Mundo 3 - Exercício 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação. Depois mostre: apenas os 5 primeiros colocados; os últimos 4 colocados; uma lista com os times em ordem alfabética; em que posição na tabela está o time da Chapecoense.
# Resolvido sem auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

brasileirao = ("Flamengo", "Cruzeiro", "Bragantino", "Palmeiras",
               "Bahia", "Fluminense", "Atlético-MG", "Botafogo",
               "Mirassol", "Corinthians", "Grêmio", "Ceará",
               "Vasco", "São Paulo", "Santos", "Vitória",
                "Internacional","Fortaleza", "Juventude", "Sport")

print("-=" *15)
print(f"Os cinco primeiros colocados são: {", ".join(brasileirao[0:5])}.")
print("-=" *15)
print(f"Os últimos colocados são: {", ".join(brasileirao[-4:])}")
print("-=" *15)
print(f"Os times em ordem alfabética: {", ".join(sorted(brasileirao))}")
print("-=" *15)
print(f"O Corinthians está na {brasileirao.index("Corinthians")+1}ª posição.")
print("-=" *15)
