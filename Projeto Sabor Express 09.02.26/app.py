import os

restaurantes = [{'nome': "Sandro's Pizzaria", 'categoria':'Pizza', 'ativo': False},
                {'nome': 'Renato Lanches', 'categoria': 'Lanchonete', 'ativo': True},
                {'nome': 'Cacau Show', 'categoria': 'Chocolate', 'ativo': False}]

def exibir_nome_do_programa ():
      '''Essa função é responsável por mostrar o titulo do programa'''
      print("""
     
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
      '''Essa função é responsável por mostrar as opções do programa'''
      print("1. Cadastrar restaurante")
      print("2. Listar restaurante")
      print("3. Alternar estado do restaurante")
      print("4. Sair\n")

def voltar_ao_menu_principal():
      '''Essa função é responsável por voltar o usuario ao menu, para não repetir códigos
      
      Imput:
      - Digitar alguma tecla para voltar ao menu

      '''
      input("\nDigite uma tecla para voltar ao menu ")
      main()

def opcao_invalida():
      '''Essa função é responsável para avisar caso a opção seja invalida'''
      print("Opção inválida!\n")
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      '''Essa função é responsável por deixar o subtitulo mais nonito, além de mostra-lo na tela'''
      os.system("cls")
      linha = '*' * (len(texto) + 4) 
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      '''Essa função é responsavel por cadastrar um novo restaurante
      
      Imputs:
      - Nome dos restaurantes
      - Categotias

      Outputs:
      - Adiciona um restaurante a lista dos restaurantes

      '''
      exibir_subtitulo('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)

      print(f"o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      voltar_ao_menu_principal()
      
def listar_restaurantes():
      '''Essa função é responsável por mostrar a lista de restaurante e suas caracteristicas
      
      Output:
      - Mostra as informações que estão na lista "restaurantes"

      '''
      exibir_subtitulo("Listando os restaurantes")
      #para cada restaurante na lista (restaurantes)

      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante ['nome']
            categoria = restaurante ['categoria']
            ativo = 'Ativado' if restaurante ['ativo'] else 'Desativado'
            print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      '''Essa função é responsável por mudar o estado do restaurante de ativado e desativado
      
      Imput:
      - Seleciona o nome do restaurante

      Output:
      - Inverte o estado do restaurante entre ativo e inativo

      '''
      exibir_subtitulo('Alterando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alternar o espaço: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso!'
                  print(mensagem)

      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

      voltar_ao_menu_principal()

def escolher_opcao():
      '''Essa função é responsável por fazer o usuario conseguir selecionar a opção escolhida
      
      Imput:
      - Seleciona a opção da lista de opções

      Output:
      - Ativa a função referente a opção escolhida
      
      '''
      try:
            opcao_escolhida = int(input("Escolha uma opção: ")) 
            # opcao_escolhida = int(opcao_escolhida)

            if opcao_escolhida == 1: 
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:        
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def finalizar_app():
      '''Essa função é responsável por mostrar que o programa foi encerrado, caso a opção 4 seja a escolhida'''
      exibir_subtitulo("Encerrando o programa") 
    
def main():
     '''Essa função é responsável por manter a ordem no que irá parecer ao iniciar o programa'''
     os.system('cls')
     exibir_nome_do_programa()
     exibir_opcoes()   
     escolher_opcao()
     

if __name__ == "__main__":
    main()