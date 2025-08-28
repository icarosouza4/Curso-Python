# Comandos Aula 11 - Cores no terminal

# Códigos ANSI para cores
# \033[ = código de escape ANSI
# 0; = reset de formatação
# 30-37 = cores do texto (preto, vermelho, verde, amarelo, azul, magenta, ciano, branco)
# 40-47 = cores do fundo (mesmas cores)
# 1; = negrito
# 4; = sublinhado
# 7; = invertido (texto e fundo trocados)

# Cores básicas do texto (30-37)
Preto = "\033[30m"
Vermelho = "\033[31m"
Verde = "\033[32m"
Amarelo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Ciano = "\033[36m"
Branco = "\033[37m"

# Cores básicas do fundo (40-47)
Fundo_preto = "\033[40m"
Fundo_vermelho = "\033[41m"
Fundo_verde = "\033[42m"
Fundo_amarelo = "\033[43m"
Fundo_azul = "\033[44m"
Fundo_magenta = "\033[45m"
Fundo_ciano = "\033[46m"
Fundo_branco = "\033[47m"

# Cores brilhantes do texto (90-97)
Preto_brilhante = "\033[90m"
Vermelho_brilhante = "\033[91m"
Verde_brilhante = "\033[92m"
Amarelo_brilhante = "\033[93m"
Azul_brilhante = "\033[94m"
Magenta_brilhante = "\033[95m"
Ciano_brilhante = "\033[96m"
Branco_brilhante = "\033[97m"

# Cores brilhantes do fundo (100-107)
Fundo_preto_brilhante = "\033[100m"
Fundo_vermelho_brilhante = "\033[101m"
Fundo_verde_brilhante = "\033[102m"
Fundo_amarelo_brilhante = "\033[103m"
Fundo_azul_brilhante = "\033[104m"
Fundo_magenta_brilhante = "\033[105m"
Fundo_ciano_brilhante = "\033[106m"
Fundo_branco_brilhante = "\033[107m"

# Estilos de formatação
Negrito = "\033[1m"
Sublinhado = "\033[4m"
Invertido = "\033[7m"
Reset = "\033[0m"  # Reset de todas as formatações

print(f"{Vermelho}Texto em vermelho{Reset}") # Exemplo 1
print(f"Este código está com um {Vermelho}ERRO{Reset} na formatação.") # Exemplo 2
