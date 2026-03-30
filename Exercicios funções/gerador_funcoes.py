# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para 
# aplicar diferentes taxas de desconto sobre os valores das compras.

# Diante deste problema, crie uma closure que gere uma função capaz de calcular o 
# preço final com um desconto fixo definido pelo usuário.

# entrada
# Digite a porcentagem de desconto: 10 

# Digite o valor da compra: 200 

# saida
# Preço final com desconto: 180.0 

def calcular_desconto(porcentagem):
    def valor(preco):
        return (preco - (preco * (porcentagem/100)))
    return valor
desconto = float(input('Digite a porcentagem de desconto: '))
preco_final = calcular_desconto(desconto)

valor = float(input('Digitr o valor da compra: '))

print(f'Precço final com desconto: {preco_final(valor)}')


# função dentro de função se chama um closure

    