# Gerador de Senhas Aleatórias

import random
import string

def gerar_senha(tamanho): # type: ignore
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # type: ignore
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada: ", senha_gerada)