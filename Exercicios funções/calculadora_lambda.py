# Joana está participando de um processo seletivo para uma vaga de desenvolvedora 
# e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar 
# e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números e 
# um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado 
# correspondente.

# entrada
# Digite o primeiro número: 10   
# Digite o segundo número: 5   
# Escolha a operação (| + | - | * | / |): + 

# saida
# O resultado é: 15 

def calculadora():
    soma = lambda n1, n2: n1 + n2
    subtracao = lambda n1, n2: n1 - n2
    multiplicacao = lambda n1, n2: n1 * n2
    divisao = lambda n1, n2: n1 / n2 if n2 != 0 else "Erro: Divisão por zero" 

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    sinal = input('Escolha a operação (| + | - | * | / |): ')

    if sinal == '+':
        print(f'O resultado é: {soma(n1, n2)}')
    elif sinal == '-':
        print(f'O resultado é: {subtracao(n1, n2)}')
    elif sinal == '*':
        print(f'O resultado é: {multiplicacao(n1, n2)}')
    elif sinal == '/':
        print(f'O resultado é: {divisao(n1, n2):.2f}')
    else:
        print('Sinal não identificado.')

calculadora()
