# Calculadora de IMC

# Solicitar peso e altura

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular IMC
imc = peso / (altura ** 2)

peso_ideal = (imc >= 18.5) and (imc <= 24.9)

print("Seu IMC é: ", imc)
print("Você está no peso ideal? ", peso_ideal)