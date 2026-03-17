# Função recursiva para fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

num = int(input("Digite um número inteiro positivo: "))
if num >= 0:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}")
else:
    print("Número inválido.")