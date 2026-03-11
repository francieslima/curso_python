# Funções
# são uma maneira de criar código que pode ser reutilizável
# 2 partes que verificam a idade do usuário => transformar em função

# def == function

def saudacao():
    print("Olá, seja bem-vindo!")

# a função precisa ser chamada/invocada

saudacao()

# parametros => uma forma de configurar a função
# mandar valores para a função e ela executa de maneira diferente

def saudacao_personalizada(nome):
    print(f"Olá {nome}, seja bem-vindo.")

saudacao_personalizada("Francies")

# Multiplos parâmetros => separados por vírgula
def apresentar_pessoa(nome, idade, profissao):
    print(f"\nDados da pessoa \nNome: {nome} \nIdade: {idade} \nProfissão: {profissao}")

apresentar_pessoa("Francies", 43, "Programador")
print("\n")

# return => instrução que retorna um valor para o programa

def soma(a, b):
    resultado = a + b
    return resultado

soma(5, 5)
x = 10

soma_x = x + soma(5, 5)
print(f"Soma_x = {soma_x}")

# ele volta o valor da função para o escopo global

# criar uma função que converte fahrenheit para celsius

# preciso criar a função, aceitar a temperatura em F
# passar pela formula de conversao (f - 32) * 5/9
# retorna o valor para o escopo global
# imprimir resultado
print("\n")
def fahrenheit_p_celsius(f):
    return (f -32) * 5/9

temp_f = 102
temp_c = fahrenheit_p_celsius(temp_f)

print(f"Temperatura em Celsius: {temp_c}")