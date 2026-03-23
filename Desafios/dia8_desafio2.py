# Calculando a distância entre dois pontos

import math

def distancia(ponto1, ponto2): # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    x1, y1 = ponto1  # type: ignore
    x2, y2 = ponto2 # type: ignore
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # type: ignore

x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

dist = distancia((x1, y1), (x2, y2))
print(f"A distancia entre os pontos é: {dist:.2f}")