#estrutura de repetição

# repetir N vezes
# onde n é o número definido pelo usuário
# ou uma condição

frutas = ["maça", "banana", "laranja"]

# for item_individual in lista:
#   bloco repetido N vezes

for fruta in frutas:
    print("Fruta: ", fruta)

print("\n")

for i in range(5):
    print("Número: ",i)

print("\n")

# while

contador = 0

while contador < 5:
    print("NUM while: ", contador)
    contador += 1

print("\n")

for i in range(10):
    if i == 5:
        break
    print("NUM for: ", i)

# break => para o loop
# continue => pula uma execução
print("\n")

for n in range(10):
    if n == 2:
        continue
    print("For in continue ", n)

print("\n")

# calcular a multiplicacao de 1 a N
# N = int(input("Digite um número: "))
# multiplicacao = 0

# for i in range(1, N + 1):
#     resultado = N * i
#     print(N, " x ", i, " = ", resultado)

print("\n")

# numeros pares e impares até 20
pares = 0
impares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares: ", pares)
print("Quantidade de ímpares: ", impares)