# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não 
# ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, 
# se necessário, exiba uma mensagem de alerta.

def monitoramento_temperatura():
    temperatura = int(input('Digite a temperatura atual: '))

    if temperatura == 25:
        print('A temperatura está ideal!')
    elif temperatura > 25:
        print('Alerta! A temperatura está acima do limite permitido.')
    else:
        print('Alerta! A temperatura está abaixo do limite permitido.')

monitoramento_temperatura()