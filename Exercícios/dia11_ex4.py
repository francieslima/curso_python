# Contador de Caracteres

texto = input("Digite um texto: ")

contagem = {}

for caractere in texto:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

print("Contagem de caracteres: ")

for caractere, quantidade in contagem.items():
    print(f"'{caractere}': {quantidade}")