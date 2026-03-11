# Trabalhando com tuplas

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero_mes = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero_mes <= 12:
    print(f"O mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("Número inválido! Por favor, digite um número entre 1 e 12.")