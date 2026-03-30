import os

def limpar_chat():
    os.system('cls')

#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_nomes = ['Daniel', 'Izabel', 'Antonio', 'Sabrina']

lista_nascimento = [2007, 2026]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

def todos_nomes():
    for nome in lista_nomes:
        print("-", nome)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

def soma_numeros_impares():
   soma_impares = 0
   for i in range(1, 11, 2):
        soma_impares += i
        print(soma_impares)

# range(1, 11, 2) -> 1 = inicio, 11 = limite, no max 10, 2 = pula de 2 em 2

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def numeros_decrescente():
    for i in range (10, 0, -1):
        print(i)

# range(10, 0, -1) -> 10 = inicio, 0 = limite, no max 1, -1 = diminuindo 1

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for 
# para imprimir a tabuada desse número, indo de 1 a 10.

def tabuada():
    limpar_chat()
    raiz = int(input('Digite o número desejado: '))
    for i in range (1, 11):
     multiplicacao = raiz*i
     print(multiplicacao)
     
#6 - Crie uma lista de números e utilize um loop for para calcular a 
# soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

























