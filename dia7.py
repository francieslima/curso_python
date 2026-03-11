# adivinhe um número

import random

print("Bem-vindo ao jogo 'Adivinhe o Número'")

# repetir um código até o usuário acertar

# gerar um número aleatório (1 - 50)
numero_secreto = random.randint(1, 50)
    # print(numero_secreto)
tentativas_restantes = 5

while True:
        
    print("Pensei num número entre 1 e 50")
    print("Você tem 5 tentativas para adivinhar")

    while tentativas_restantes > 0:

        # palpite do usuário (input)
        palpite = input("Digite um número: ")

        # validação para checar se o usuário digitou um número
        if not palpite.isdigit():
            print("Entradda inválida! Por favor, digite um número entre 1 e 50")
            continue

        # converter palpite para inteiro
        palpite = int(palpite)
        
        # ver se o número está no intervalo estipulado
        if palpite < 1 or palpite > 50:
            print("O número deve ser entre 1 e 50")
            continue
        
        # descontar tentativas
        tentativas_restantes -= 1

        # verificar se o palpite está correto

        if palpite == numero_secreto:
            print(f"\nVocê acertou! \nVocê ainda tinha {tentativas_restantes} tentativas.")        
            break
        elif palpite < numero_secreto:
            print("\nO número é maior que esse.")
        else:
            print("\nO número é menor que esse")

        print(f"Tentativas restantes: {tentativas_restantes}")
    
    # while else, para quando as tentativas acabarem
    else:
        print(f"\nVocê perdeu! \nO número secreto era {numero_secreto}.")
    
    # perguntar se o jogador quer jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (s/n)").lower()

    if jogar_novamente != "s":
        print("Obrigado e até a próxima...")
        break
    else:
        print("\n")
        tentativas_restantes = 5
        