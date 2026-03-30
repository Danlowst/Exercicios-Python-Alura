# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize
#  uma estrutura if elif else para determinar em qual quadrante do plano 
# cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

def coordenadas_plano():
    print('Plano Cartesiano')
    x = int(input('Insira a coordenada x: '))
    y = int(input('Insira a coordenada y: '))

    #primeiro quadrante
    if x > 0 and y > 0:
        print('\nAs coordenadas se encontram no primeiro quadrante')

    #segundo quadrante
    elif 0 > x and y > 0:
        print('\nAs coordenadas se encontram no segundo quadrante')
    
    #terceiro quadrante
    elif x < 0 and y < 0:
        print('\nAs coordenadas se encontram no terceiro quadrante')

    #quarto quadrante
    elif x > 0 and 0 > y:
        print('\nAs coordenadas se encontram no quarto quadrante')

    #quinto quadrante
    else:
        print('\nAs coordenadas se encontram no quadrante de origem')
    
coordenadas_plano()