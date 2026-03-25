# Verificação de Palíndromo

palavra = input("Digite uma palavra: ").lower()
palavra_sem_espaco = palavra.replace(" ", "")
if palavra_sem_espaco == palavra_sem_espaco[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")