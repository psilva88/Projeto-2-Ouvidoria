from main_metodos_teste import *
from operacoesbd_english import *
conn = createConnection ('127.0.0.1', 'root', 'xxxx', 'ouvidoria_project')
option = -1
manifestation = listDataBase(conn, 'select * from manifestation')
 
print("Bem-vindo a ouvidoria da Universidade XYZ, na qual sua voz é importante!")
seunome = input("Por favor, digite seu nome usuário: ")
print(f"Olá {seunome}, o que você gostaria de fazer?")

while option != 7:
    option = int(input("\n Selecione uma das opções abaixo: \n 1) 🔍 Listagem das Manifestações \n 2) 📂 Listagem das manifestações filtradas por tipo \n 3) ➕ Criar uma nova manifestação \n 4) 📊 Exibir a quantidade total de manifestações \n 5) 🔎 Pesquisar uma manifestação através do código \n 6) 🗑️  Excluir uma manifestação pelo código \n 7) 🚪 Sair do sistema \n" ))

    if option == 1:
        opcao1(conn)  

    elif option == 2:
        opcao2(conn)

    elif option == 3:
        opcao3(conn)

    elif option == 4:
        opcao4(conn)

    elif option == 5:
        opcao5(conn)

    elif option == 6:
        opcao6(conn)

    elif option == 7:
        opcao7(seunome)

    else:
        print("Opção inválida.")
