'''
•🔍Listagem de todas as manifestações registradas;

•📂Listagem de manifestações filtradas por tipo (reclamação, sugestão ou elogio);

•➕Criar uma nova manifestação e armazená-la no sistema;

•📊Exibir a quantidade total de manifestações registradas;

•🔎Pesquisar uma manifestação específica através do código único;

•🗑️Excluir uma manifestação pelo código de identificação;

•🚪Sair do sistema de ouvidoria de forma segura.
'''
from operacoesbd_english_cirugia import *
conn = createConnection ('127.0.0.1', 'root', '99998888', 'ouvidoria_project')
option = -1
manifestation = listDataBase(conn, 'select * from manifestation')
 
print("Bem-vindo a ouvidoria da Universidade XYZ, na qual sua voz é importante!")
seunome = input("Por favor, digite seu nome usuário: ")
print(f"Olá {seunome}, o que você gostaria de fazer?")

while option != 7:
    option = int(input("\n Selecione uma das opções abaixo: \n 1) 🔍 Listagem das Manifestações \n 2) 📂 Listagem das manifestações filtradas por tipo \n 3) ➕ Criar uma nova manifestação \n 4) 📊 Exibir a quantidade total de manifestações \n 5) 🔎 Pesquisar uma manifestação através do código \n 6) 🗑️  Excluir uma manifestação pelo código \n 7) 🚪 Sair do sistema \n" ))
    
    
    if option == 1:
        consultationListManifestations = "select * from manifestation"
        manifestation = listDataBase(conn, consultationListManifestations)
        if len(manifestation) > 0:
            print("Aqui está as manifestações cadastradas: \n")
            for manifest in range(len(manifestation)):
                print(f"Código da Manifestação: {manifestation[manifest][0]} - {manifestation[manifest][1]}.")
        else:
            print("Sem manifestações no sistema.")


    elif option == 2:
        print("Por favor digite o tipo da sua manifestação: \n 1) 😡 Reclamação \n 2) 💡 Sugestão \n 3) 🌟 Elogio")
        


    elif option == 3:
        newManifestation = input("Por favor digite a sua manifestação: ")
        while True:
            if len(newManifestation) < 1:
                newManifestation = input("Manifestação inválida. Por favor digite novamente uma manifestação válida: ")
            elif len(newManifestation) > 1:
                break
        insertConsultation = "insert into manifestation (manifestacao) values (%s)"
        data = [newManifestation]
        insertInDataBase(conn, insertConsultation, data)
        cursor = conn.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        position = cursor.fetchone()[0]
        cursor.close()
        if len(newManifestation) > 0:
            print(f"Manifestação cadastrada com sucesso! Seu código é: {position}")
        

    elif option == 4:
        consultationListManifestations = 'select count(*) from manifestation'
        resultado = listDataBase(conn, consultationListManifestations)
        manifestationQuantity = resultado[0][0]

        if manifestationQuantity > 0:
            print(f"Temos {manifestationQuantity} manifestações cadastradas no sistema.")
        else:
            print("Não há manifestações cadastradas no sistema.")

    
    elif option == 5:
        consultationListManifestations = "select count(*) from manifestation"
        resultado = listDataBase(conn, consultationListManifestations)
        quantidade = resultado[0][0]

        if quantidade == 0:
            print("Não há manifestações cadastradas no sistema.")
        else:
            while True:
                searchManifestation = int(input("Digite o código da manifestação que deseja encontrar: "))
                data = [ searchManifestation ]
                consultationSearch = "select * from manifestation where codigo = %s"
                manifestation = listDataBase(conn, consultationSearch, data)

                if len(manifestation) == 0 or searchManifestation < 1:
                    print("Manifestação não encontrada, tente novamente!")
                else:
                    print(f"Manifestação encontrada: {manifestation[0][1]}")
                    break


    elif option == 6:
        while True:
            deleteManifestation = int(input("Digite o código da manifestação que deseja excluir: "))
            data = [ deleteManifestation ]
            consultationDelete = "select * from manifestation where codigo = %s"
            manifestation = listDataBase(conn, consultationDelete, data)
            if len(manifestation) == 0 or deleteManifestation < 1:
                deleteManifestation = int(input("Manifestação não encontrada, tente novamente: "))
            else:
                deleteConsultation = "delete from manifestation where codigo = %s"
                deleteDataBase(conn, deleteConsultation, data)
                print(f"Manifestação com o código {deleteManifestation} excluída com sucesso.")
                break
    
    elif option == 7:
        print (f"Agradecemos pelo uso {seunome}. ")
    

    else:
        print("Opção inválida.")

endConnection(conn)
