#1 - Imprima a frase: Python na Escola de Programação da Alura.
print( 'Python na Escola de Programação da Alura\n')


#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

print(f'\nMeu nome é {nome} e tenho {idade} anos.\n')


#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
print('A \n L\n U\n R\n A\n')
print('A','L','U','R','A',sep='\n')


#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável 
# e arredondado para apenas duas casas decimais. Para facilitar, utilize:
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')
print('O valor arredondado de pi é:', round(pi, 2))

#match expressão:
    #case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    #case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    #     outros casos ...
    #case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.