#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def nome_senha():
    print('Criação de conta:\n ')
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    print('\nLogin: ')

    nome_login = input('\nDigite seu usuário: ')
    senha_login = input('Digite sua senha: ')

    if nome == nome_login and senha == senha_login:
        print('\nLogin efetuado com sucesso')
    else:
        print('\nUsuario ou senha incorretos')


nome_senha()
