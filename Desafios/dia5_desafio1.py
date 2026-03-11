# Calculando Fatorial de um número

N = int(input("Digite um número inteiro positivo: "))

fatorial = 1

if N < 0:
    print("Não existe fatorial de número negativo.")
elif N == 0 or N == 1:
    print(f"O fatorial de {N} é 1.")
else:
    for i in range(1, N+1):
        fatorial *= i
    print(f"O fatorial de {N} é {fatorial}.")