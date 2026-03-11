# Calculadora de tarifas de táxi

distancia = float(input("Digite a distância percorrida em km: "))

tarifa_basica = 4.00
custo_por_km = 0.25

valor_total = tarifa_basica + (custo_por_km * distancia)

print(f"Valor total da corrida: R$ {valor_total:.2f}")