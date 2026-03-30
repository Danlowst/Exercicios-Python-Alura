# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas
#  no dia. As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números
#  e exiba o total.

# entrada
# Digite os valores das vendas: 100 250 300 

# saida
# O total de vendas foi: 650 

def total():
    valores = input('Digite os valores das vendas: ').split()
    # split separa as palavras separas por espaços e coloca numa lista, como string

    total = sum(map(float, valores))
    # map é utilizado para tranformar cada um da lista valores em float e, o sum é utilizado para
    # somar cada número da lista

    print(f'O total de vendas foi: {total}')

