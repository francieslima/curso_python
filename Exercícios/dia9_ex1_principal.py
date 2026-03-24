# Criando um módulo de Conversão de Temperaturas - Parte 2
# Programa_principal.py

import dia9_ex1_conversoes

temperatura_c = float(input("Digite a temperatura em Celsius: "))
temperatura_f = dia9_ex1_conversoes.celsius_para_fahrenheit(temperatura_c)
temperatura_k = dia9_ex1_conversoes.celsius_para_kelvin(temperatura_c)

print(f"{temperatura_c:.2f}°C equivalem a {temperatura_f:.2f}°F e {temperatura_k:.2f}K")