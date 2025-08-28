# Mundo 3 - Exercício 077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# Resolvido com auxílio.

Preto = "\033[30m"

print(f"{Preto}")

palavras = ("aprender","programar","linguagem","python",
            "curso","gratis","estudar","praticar",
            "trabalhar","mercado","programador","futuro")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
