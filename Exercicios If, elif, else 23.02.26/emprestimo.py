# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
# 
# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.

# Crie um programa que receba como entrada a renda mensal de Pedro e o valor 
# da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou 
# negado com base nas condições acima.

#Digite o valor da sua renda mensal
#Digite o valor da parcela desejada
#empréstimo negado: parcela acima de 30% da renda.

def emprestimo():
    try: 
        renda_mensal = float(input('Digite o valor da sua renda mensal: '))
        parcela = float(input('Digite o valor da parcela desejada: '))

        if renda_mensal > 2000 and parcela < 0.3 * renda_mensal:
            print('Empréstimo aprovado!')
        elif renda_mensal <= 2000:
            print('Empréstimo negado: Renda insuficiente')
        else:
            print('Empréstimo negado: Parcela acima de 30% da renda.')
    except ValueError:
        print('Valor inválido.')

emprestimo()