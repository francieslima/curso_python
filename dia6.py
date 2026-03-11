# listas (array) e tupplas
# interligados com os loops - estruturas de repetição

carros = ["bmw", "fiat", "ford"]

# os índices começam a contar de 0
print(carros[0])
print(carros[2])

# adicionando novos itens
carros.append("vw")

print(carros[3])

carros[0] = "bmw eletrica"

print(carros[0])
print(carros)

print("\n")
# remover um item do arrey
carros.remove("fiat")

print(carros)

# métodos => append (adicionar), remove (remover)

# visualizar a quantidade de itens que um arrey possui
print("\n")

print(len(carros))

# verificar se um item está presente no array
print("\n")

if "bmw eletrica" in carros:
    print("Achei!")

print("\n")

# tuplas
# são criadas dentro de parênteses (1, 2, 3)
# não podem ser modificadas

cores = ("vermelho", "verde", "laranja", "roxo")
print(cores)
print(cores[1])

print("\n")

for cor in cores:
    print("Cor: ",cor)

print("\n")

print(len(cores))

if "vermelho" in cores:
    print("Achei!")

print("\n")


