# tratamento de erros e exceções
# criar programas que precisam estar a prova de falhas

# try, except, else, finally

# try => Tentando executar o bloco de comandos
# except => Trata possíveis erros de execução
# else => executa outro bloco caso o try tenha sucesso
# finally => finaliza a execução do bloco e roda independente de erros


try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: o arquivo não existe")
else:
    print("Arquivo lido!")
    print(conteudo)
finally:
    print("Operação finalizada")
    if 'arquivo' in locals():
        arquivo.close()
        print("Arquivo fechado.")

print("\n")

try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except (ValueError, ZeroDivisionError) as error:
    print("Erro: ", error)
#    print("Entrada inválida, tente novamente.")
#except ZeroDivisionError:
#    print("Erro! Divisão por 0.")
else:
    print("O resultado é: ", resultado)
finally:
    print("Operação concluída!")