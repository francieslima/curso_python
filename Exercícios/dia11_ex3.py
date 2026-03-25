# União e Interseção de Conjuntos

numeros1 = input("Digite números separados por espaço para o primeiro conjunto: ").split()
numeros2 = input("Digite números separados por espaço para o segundo conjunto: ").split()

conjunto1 = set(numeros1)
conjunto2 = set(numeros2)

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)

print("União dos conjuntos: ", uniao)
print("Interseção dos conjuntos: ", intersecao)