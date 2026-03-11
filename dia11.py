# dicionários
# semelhante aos objetos em outras linguagens

# array []
# tupla ()
# dicionários {}

aluno = {
    "nome": "Francies",
    "profissao": "Programador",
    "idade": 43
}

# "nome_da_chave": "valor", que pode ser texto, número ou array

print(aluno["nome"])
print(f"O nome dele é {aluno['nome']} e a sua profissão é {aluno['profissao']}.")

# adicionando e atualizando as chaves
aluno["nota"] = 15
aluno["profissao"] = "Engenheiro"
print(aluno)

# remoção de chave

del aluno["profissao"]

print(aluno)

print("\n")

# conjunto => set - lê uma lista com números repetidos e retorna
# esta lista apenas com valores únicos

lista = [1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 7]
lista_unica = set(lista)

print(lista)
print(lista_unica)

# adicionando novos valores ao conjunto
lista_unica.add(8)
lista_unica.add(6)

# excluindo valores do conjunto
lista_unica.remove(2)

print(lista_unica)

print("\n")

# união de conjuntos
lista_b = {1, 3, 5, 10}

uniao = lista_unica.union(lista_b)
print(uniao)

# interseção
intersecao = lista_unica.intersection(lista_b)
print(intersecao)

# diferença -> O inverso da interseção
diferenca = lista_unica.difference(lista_b)
print(diferenca)

print("\n")

# criar uma função que vai adicionar a nota da Prova A a um aluno

def adicionar_nota(aluno):
    aluno["prova_a"] = int(input("Digite a nota A:"))

aluno_teste = {
    "nome": "João"
}

adicionar_nota(aluno_teste)
print(aluno_teste)

print("\n")

# verificar as palavras únicas de uma frase (set)
frase = input("Digite uma frase: ")

# separando as palavras da frase
palavras = frase.split()
print(palavras)

print("\n")

palavras_unicas = set(palavras)
print(palavras_unicas)