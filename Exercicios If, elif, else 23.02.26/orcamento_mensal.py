# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um 
# limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas 
# despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou 
# o limite ou ainda está dentro do orçamento.

#digite o total de despesas do mês (R$)
#atenção! Você ultrapassou o limite do orçamento.

def orcamento():

    try:
        total = float(input('Digite o total de despesas do mês (R$): '))
        if total <= 3000:
            print('Você está dentro do limite do orçamento')
        else:
            print('Atenção! Você ultrapassou o limite do orçamento')
    except ValueError:
        print('Valor não identificado!')

orcamento()