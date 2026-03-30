# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
# Ela deseja criar um programa que exiba uma saudação personalizada dependendo da 
# hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

# Se for antes das 12h, exibir "Bom dia";

# Entre 12h e 18h, exibir "Boa tarde";

# Após 18h, exibir "Boa noite".

# Entrada
# Digite a hora atual (0-23): 15 

# Saida
# Boa tarde! 

def saudacao(horario):
    if horario < 12:
        return 'Bom dia'
    elif  18 < horario:
        return 'Boa Tarde'
    else:
        return 'Boa noite'

hora = int(input('Digite a hora atual (0-23): '))
print(saudacao(hora))     