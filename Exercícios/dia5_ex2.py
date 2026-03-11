# Calculando a Soma dos númeor s de 1 a N

N = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, N+1):
    soma += i

print("A soma dos números de 1 a ", N, " é: ", soma)