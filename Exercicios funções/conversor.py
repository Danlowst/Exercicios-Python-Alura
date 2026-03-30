# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os 
# números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar 
# buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente 
# como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica 
# se a conversão foi feita corretamente e todos os números de telefone são inteiros:

# Entrada
# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

# Saida
# Todos os números foram convertidos corretamente! 

def conversor(telefones):
        return [int(telefone) for telefone in telefones]

def verificacao(telefones):
        for tell in telefones:
                if not isinstance(tell, int):
                        return 'Erro na conversão.'
                
        return 'Todos os números fora convertidos corretamente!'
    

numeros = ["11987654321", "21912345678", "31987654321", "11911223344"]

telefones_convertidos = conversor(numeros)

print(verificacao(telefones_convertidos))