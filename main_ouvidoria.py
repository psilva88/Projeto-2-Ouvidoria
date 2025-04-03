'''
•🔍Listagem de todas as manifestações registradas;

•📂Listagem de manifestações filtradas por tipo (reclamação, sugestão ou elogio);

•➕Criar uma nova manifestação e armazená-la no sistema;

•📊Exibir a quantidade total de manifestações registradas;

•🔎Pesquisar uma manifestação específica através do código único;

•🗑️Excluir uma manifestação pelo código de identificação;

•🚪Sair do sistema de ouvidoria de forma segura.
'''
from operacoesbd_english import *
conn = createConnection('localhost', 'root', '@mysqlberna2006', 'ouvidoria_project')
option = -1
manifestation = listDataBase(conn, 'select * from manifestation')

print("Bem-vindo a ouvidoria da Universidade XYZ, na qual sua voz é importante!")

while option != 6:
    option = int(input("\n Selecione uma das opções abaixo: \n 1) Listagem das Manifestações \n 2) Criar uma nova Manifestação \n 3) Exibir quantidade de manifestações \n 4) Pesquisar uma manifestação por código \n 5) Excluir uma manifestação por código \n 6) Sair do Sistema\n"))
    
    if option == 1:
        consultationListManifestations = "select * from manifestation"
        manifestation = listDataBase(conn, consultationListManifestations)
        if len(manifestation) > 0:
            print("Aqui está as manifestações cadastradas: \n")
            for manifest in range(len(manifestation)):
                print(f"{manifest+1} - {manifestation[manifest][1]}")
        else:
            print("Sem manifestações no sistema.")
                

    elif option == 2:
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
        

    elif option == 3:
        consultationListManifestations = 'select count(*) from manifestation'
        resultado = listDataBase(conn, consultationListManifestations)
        manifestationQuantity = resultado[0][0]

        if manifestationQuantity > 0:
            print(f"Temos {manifestationQuantity} manifestações cadastradas no sistema.")
        else:
            print("Não há manifestações cadastradas no sistema.")

    
    elif option == 4:
        while True:
            searchManifestation = input("Digite o código da manifestação que deseja encontrar: ")
            data = [ searchManifestation ]
            consultationSearch = "select * from manifestation where codigo = %s"
            manifestation = listDataBase(conn, consultationSearch, data)
            if len(manifestation) == 0:
                print("Manifestação não encontrada, tente novamente!")
            else:
                print(f"Manifestação encontrada: -{manifestation [0][1]}")
                break

    elif option == 5:
        manifestationCode = int(input("Digite o código da manifestação a remover: "))
        while True:
            if manifestationCode < 1:
                manifestationCode = int(input("Manifestação inválida. Por favor digite novamente uma manifestação válida: "))
            elif manifestationCode > 1:
                break
        removeConsultation = "delete from manifestation where codigo = %s"
        dados = [ manifestationCode ]

        changedLines = deleteDataBase(conn,removeConsultation,dados)
        if changedLines == 0:
                    print("Não existe manifestação para o código informado, tente novamente: ")
        else:
            print("Manifestação removida com sucesso!")
        
    elif option == 6:
        print ("Agradecemos pelo uso.")
    

    else:
        print("Opção inválida.")

endConnection(conn)
