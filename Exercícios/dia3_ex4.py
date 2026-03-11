# Sistema de Acesso

# Dados do usuário

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

# Verificar acesso

acesso_concedido = (senha_inserida == senha_correta) and not usuario_bloqueado

print("Acesso concedido? ", acesso_concedido)