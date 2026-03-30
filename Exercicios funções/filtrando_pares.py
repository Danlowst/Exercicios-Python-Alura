# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e 
# precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

# Crie um programa que receba uma lista de números e exiba apenas os pares usando a 
# função filter().

# entrada
# Digite os números separados por espaço: 1 2 3 4 5 6 

# saida
# Números pares: 2 4 6 

def pares():
    numeros = input("Digite os números separados por espaço: ").split() 
    pares = filter(lambda x: int(x) % 2 == 0, numeros) 
    print("Números pares:", " ".join(pares)) 

    # o filter é utilizado para filtrar os numeros na lista "numeros" e, o lambda é utilizado da
    # seguinte forma:
    # o lambda de x são os numeros que estão na lista
    # quando há o int(x), transforma as strings da lista em inteiros e logo após, colocam na
    # equação, por fim, o escrito "numeros" no final, é para o filter saber em qual lugar filtar

    # ja o join() tem função de unir os numeros filtrados em uma unica string