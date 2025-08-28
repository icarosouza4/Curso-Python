# Mundo 2 - Exercício 062 - Melhore o DESAFIO 061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} -", end=" ")
    termo += razao
    cont += 1
print("Deseja mostrar mais termos? [S/N]")

opcao = str(input("Digite a opção desejada: ")).strip().upper()

quantidade = 0

while opcao == "S":
    print("Quantos termos você quer mostrar a mais? ")
    quantidade = int(input("Digite a quantidade de termos: "))
    while quantidade > 0:
        print(f"{termo} -", end=" ")
        termo += razao
        quantidade -= 1
    print("Deseja mostrar mais termos? [S/N]")
    opcao = str(input("Digite a opção desejada: ")).strip().upper()

print("FIM")
