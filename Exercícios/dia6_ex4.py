# Ordenando uma lista

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

# Ordem crescente
numeros_crecente = sorted(numeros)
print("Números em ordem crescente:", numeros_crecente)

# Ordem decrescente
numeros_decrescente = sorted(numeros, reverse=True)
print("Números em ordem decrescente:", numeros_decrescente)