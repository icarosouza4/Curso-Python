# Mundo 3 - Exercício 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.
# Resolvido sem auxílio.

Preto = "\033[30m"

print(f"{Preto}")

def escreva(msg):
    t = len(msg) + 4
    
    print("~" * t)
    print(f"  {msg}")
    print("~" * t)
    

escreva("ICARO CESAR ALMEIDA DE SOUZA")
escreva("SISTEMAS DE INFORMÇÃO")
escreva("2º PERÍODO")
