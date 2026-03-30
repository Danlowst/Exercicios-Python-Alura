# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir 
# três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, 
# o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do 
# projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

def organizacao_projeto():
    projeto_A = int(input('Informe os dias para a atividade A: '))
    projeto_B = int(input('Informe os dias para a atividade B: '))
    projeto_C = int(input('Informe os dias para a atividade C: '))

    soma = projeto_A + projeto_B + projeto_C

    if projeto_A < 0 or projeto_B < 0 or projeto_C < 0:
        print('Erro: Os dias não podem ser negativos')
    else:
        print(f'Dias totais: {soma}')

organizacao_projeto()
    