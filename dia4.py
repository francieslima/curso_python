# condicionais -> estruturas if, else

idade = 16

# estrutura do if
# o bloco do if só será executado se a condição for verdadeira

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

print("\n")

# meia entrada => menor de 18 anos OU esteja estudando em
# escola/faculdade pública

estuda_rede_publica = False

if idade < 18 or estuda_rede_publica:
    print("Tem direito a meia entrada")

print("\n")

# nota: A, B e C
# > 9 = A, > 8 = B, > 6 = C

nota = 6.5

# elif  => else if
# uma condição intermediária entre o if e else

if nota > 9:
    print("O seu conceito é A")
elif nota > 8:
    print("O seu conceito é B")
elif nota > 6:
    print("O seu conceito é C")
else:
    print("Você deve melhorar a sua nota...")

print("\n")
# climas: ensolarado, chuvoso, nublado

clima = "chuvoso"

if clima == "ensolarado":
    print("O dia está ensolarado!")
elif clima == "chuvoso":
    print("O dia está chuvoso.")
else:
    print("O dia está nublado.")

print("\n")

# comissao de vendas
# valor_venda > 1000 = recebe .5%
# valor_venda > 500 = recebe 1%
# valor_venda < 500 = recebe 2%

valor_venda = 1200

if valor_venda > 1000:
    print("Comissão de 0.5%")
    comissao = valor_venda * .005
    print("A comissão da venda foi de R$:", comissao)
elif valor_venda > 500:
    print("Comissão de 1%")
    comissao = valor_venda * .01
    print("A comissão da venda foi de R$:", comissao)
else:
    print("Comissão de 2%")
    comissao = valor_venda * .02
    print("A comissão da venda foi de R$:", comissao)


print("\n")
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número ", numero, " é maior que zero")
else:
    print("O número ", numero, " é menor que zero")