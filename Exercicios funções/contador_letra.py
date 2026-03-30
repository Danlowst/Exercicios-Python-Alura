# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra 
# de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

# Entrada
# Digite uma palavra: tecnologia 

#Saida
# Essa palavra tem 10 caracteres. 

def contar_letras(contagem):
    return len(contagem)

palavra = input('Digite uma palavra: ')
print(f'Essa palavra tem {contar_letras(palavra)} letras.')
