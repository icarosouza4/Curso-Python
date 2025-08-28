# Comandos Aula 23 - Tratamento de erros e exceções

# try: (Tentativa de execução.)
# except: (Falha na execução.)
# else: (Êxito na execução.)
# finally: (Fim da execução.)

try:
    a = int(input("Numeraodr: "))
    b = int(input("Denominador: "))
    resultado = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com o tipo de dado utilizado.")
except ZeroDivisionError:
    print("Não é possível dividir um número por 0.")
except KeyboardInterrupt:
    print("O usuário não informou dados.")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}.") #Exibe a causa do erro.
else:
    print(f"O resultado foi {resultado:.1f}.")
finally:
    print("Encerrando...")
