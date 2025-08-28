# Mundo 3 - Exercício 083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.
# Resolvido com auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

expressao = str(input("Digite a expressão: "))
pilha = []

for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Esta expressão é válida.")
else:
    print("Esta expressão é inválida.")
    