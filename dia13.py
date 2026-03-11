# como trabalhar com arquivos em Python

# uma forma de ler o arquivo todo

with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print("\n")
# ler o arquivo linha por linha
with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip()) # o strip elimina o \n\n interno, deixando apenas um \n
        break

# escrever em um arquivo

# o método .write() criar o arquivo, caso ele não exista
# mas sobrescreve o arquivo, caso exista. Apagando o conteúdo anterior
with open("saida.txt", "w") as arquivo:
    arquivo.write("Nova linha \n")
    arquivo.write("Nova linha 2\n")

# adicionar linhas ao arquivo existente
with open("saida.txt", "a") as arquivo:
    arquivo.write("Nova linha 3 \n")
    arquivo.write("Nova linha 4\n")

# O método open("nome arquivo", "tipo de ação") possui 3 ações
# r - read => ler
# w - write => escrever
# a - append => adicionar

# Arquivo CSV -> comma separated values
import csv

with open("contatos.csv", "w", newline='') as arquivo_csv:
    # cabeçalho (colunas)
    # dados
    # dados

    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Profissão', 'Idade'])
    escritor.writerow(['Francies', 'Profissão A', 43])
    escritor.writerow(['João', 'Profissão B', 18])
    escritor.writerow(['Maria', 'Profissão C', 34])

# Json = Javascript object notation (APIs)

import json

dados = {
    'nome': 'Francies',
    'idade': 43,
    'profissao': 'Programador'
}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)