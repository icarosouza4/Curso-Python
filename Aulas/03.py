# Comandos Aula 7 - Operadores aritméticos

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

soma = n1 + n2 # Operador de adicção.
multiplicação = n1 * n2 # Operador de multiplicação.
divisão = n1 / n2 # Operador de divisão.
potência = n1 ** n2 # Operador de potenciação.
divisão_inteira = n1 // n2 # Operador de divisão inteira.(Apenas o valor inteiro da divisão, ou seja, ignora o resto da divisão.)
resto_da_divisão = n1 % n2 # Operador de resto da divisão.

# Ordem de precedência
# 1 = ()
# 2 = **
# 3 = * / // % #Calcula na ordem de exibição.
# 4 = + - #Calcula na ordem de exibição.

print("A soma vale: {}.".format(soma))
print("A multiplicação vale: {}.".format(multiplicação))
print("A divisão vale: {}.".format(divisão))
print("A potenciação vale: {}.".format(potência))
print("A divisão inteira vale: {}.".format(divisão_inteira))
print("O resto da divisão vale: {}.".format(resto_da_divisão))
