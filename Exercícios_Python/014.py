# Mundo 1 - Exercício 014 - Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.
# Resolvido sem auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

temperatura = float(input("Informe a temperatura em °C: "))

fahrenheit = (temperatura * 1.8) + 32

print(f"A temperatura de {temperatura}°C corresponde a {fahrenheit}°F.")
