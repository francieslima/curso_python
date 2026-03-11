# Pedra, papel e tesoura

import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {usuario}")
print(f"O computador escolheu: {computador}")

if (usuario == computador):
    print("Empate")
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
        print("Você venceu!")
elif usuario in opcoes:
      print("Você perdeu.")
else:
      print("Opção inválida")