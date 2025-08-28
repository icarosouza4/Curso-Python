# Mundo 3 - Exercício 090 - Faça um programa que leia nome e média de um aluno, guardando em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

aluno = dict()

aluno["nome"] = str(input("Nome: "))
aluno["média"] = float(input(f"Média de {aluno["nome"]}: "))

if aluno["média"] >= 7:
    aluno["situação"] = "aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "em recuperação"
else:
    aluno["situação"] = "reprovado"

print("=-"*10)

for k,v in aluno.items():
    print(f"-> {k} é igual a {v}.")
    
print("=-"*10)

