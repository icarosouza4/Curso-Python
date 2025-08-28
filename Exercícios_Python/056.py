# Mundo 2 - Exercício 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

soma = 0
nome_do_homem_mais_velho = ""
idade_do_homem_mais_velho = 0
mulheres_menores_20 = 0

for pessoa in range(1,5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(pessoa)))
    idade = int(input("Digite a idade da {}ª pessoa: ".format(pessoa)))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    if sexo == "M":
        print("Pessoa do sexo masculino registrada.")
    elif sexo == "F":
        print("Pessoa do sexo feminino registrada.")
    else:
        print("Opção inválida.")
    if sexo == "M":
        if idade > idade_do_homem_mais_velho:
            idade_do_homem_mais_velho = idade
            nome_do_homem_mais_velho = nome
    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1
    soma += idade

print("A média de idade do grupo é de {} anos.".format(soma / 4))
print("O homem mais velho tem {} anos e se chama {}.".format(idade_do_homem_mais_velho, nome_do_homem_mais_velho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheres_menores_20))
