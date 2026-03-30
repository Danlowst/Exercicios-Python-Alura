#6 - Crie uma lista de números e utilize um loop for para calcular a 
# soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exc


def adicionar_numeros():
    lista_somatoria = []
    somatoria = int(input('Digite os números para a soma: '))
    lista_somatoria.append(somatoria)
    
def resultado():
    soma = 0
    for somatoria in lista_somatoria:
        soma +=somatoria
        print(somatoria)

def escolha():
    os.system('cls')
    print('Somatória\n')
    print('1. Inserir números\n 2. Ver resultado')
    
    try:
        opcao_escolhida = int(input('Digite o número da opção escolhida: '))
        
        if opcao_escolhida == 1:
            adicionar_numeros()
        elif opcao_escolhida == 2:
            resultado()
    except:
        print('Dado não identificado, clique qualquer tecla para continuar')
        main()
        
def main():
    escolha()

#7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.