# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades 
# com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento 
# e o ano atual e retorne à idade correspondente.

# Entrada
# Digite o ano de nascimento: 2005  

# Digite o ano atual: 2025 

# Saida
# A idade é 20 anos. 





def calcular_idade():
    
    ano1 = int(input('Digite o ano de nascimento: '))
    ano2 = int(input('\nDigite o ano atual: '))
    idade = ano2 - ano1
    print(f'\nA idade é {idade} anos.')

calcular_idade()


def calcular_idade(ano_nascimento, ano_atual): 
    return ano_atual - ano_nascimento 
 
nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.") 