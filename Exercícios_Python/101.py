# Mundo 3 - Exercício 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
# Resolvido sem auxílio.

Azul = "\033[34m"

print(f"{Azul}")

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    
    if idade >= 18 and idade <= 70:
        return f"Sua idade é {idade} e seu voto é OBRIGATÓRIO."
    elif idade < 18 and idade >= 16 or idade > 70:
        return f"Sua idade é {idade} e seu voto é OPCIONAL."
    else:
        return f"Sua idade é {idade} e seu voto é NEGADO."


print("-="*20)
print(voto(int(input("Em que ano você nasceu? "))))
print("-="*20)
