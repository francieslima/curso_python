# Verificador de Palíndromo

def eh_palindromo(texto): # type: ignore
    texto = ''.join(char.lower() for char in texto if char.isalnum()) # type: ignore
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")