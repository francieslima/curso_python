# operadores aritméticos

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# ** exponenciação
# // divisão inteira
print("\n")
print(a // b)
print(a / b)
print(a % b)

# operadores de comparação
x = 10
y = 5
print("\n")
print(x > 5)
print(x < y)
print( x != y)

# maior ou igual
print( 5 >= 5)
# menor ou igual
print(5 <= 1)

# operadores lógicos
# AND, OR e NOT

print("\n")
idade = 20
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira

print(pode_dirigir)


# AND só é verdadeiro quando ambas as operações forem verdadeiras
# OR é verdadeiro quando PELO MENOS uma operação é verdadeira

eh_estudante = False
idade = 60

# 1 igual (=) é atribuição
# 2 iguais (==) é comparação

print("\n")
meia_entrada = eh_estudante == True or idade >= 60

print(meia_entrada)

# NOT inverte o valor de um booleano

chovendo = True
nao_chovendo = not chovendo

print("Chovendo ", chovendo)
print("Não Chovendo ", nao_chovendo)

# revisão
print("\n")

nota = 8
frequencia = 60

if(nota >=7 and frequencia >=80):
    passou = True
else :
    passou = False

print("O aluno passou? ", passou)

print("\n")

