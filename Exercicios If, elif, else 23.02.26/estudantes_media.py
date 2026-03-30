# Uma professora precisa de um programa que ajude a calcular a média final dos alunos 
# e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
# 
# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado

# Escreva um programa que receba três notas como entrada e calcule a média final. 
# Com base na média, exiba a situação do aluno.

#Digite a primeira nota
#Digite a segunda nota
#Digite a terceira nota
#média
#aprovado ou reprovado

def resultado():
    
    try:
        nota_1 = float(input('Digite a primeira nota: '))
        nota_2 = float(input('Digite a segunda nota: '))
        nota_3 = float(input('Digite a terceira nota: '))

        media = (nota_1 + nota_2 + nota_3)/3

        print(f'Média: {media:.1f}')

        if media >= 7:
            print('Aprovado')
        elif 5 <= media < 7:
            print('Recuperação')
        else:
            print('Reprovado')
    except ValueError:
        print('Erro! Valor não identificado.')

resultado()