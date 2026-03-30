# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é
#  par ou ímpar

numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print('Este número é par')
else:
    print('Este número é impar\n')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar
#  a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def categoria_idade():
    idade = int(input('Digite a sua Idade: '))
    if 0 < idade <= 12:
        print('Você é criança')
    elif 13<= idade <= 18:
        print('Você é adolescente')
    elif idade > 18:
        print('Você é adulto')
    else:
        print('Valor inválido')

categoria_idade()


