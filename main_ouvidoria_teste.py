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
conn = createConnection ('127.0.0.1', 'root', 'xxxx', 'ouvidoria_project')
option = -1
manifestation = listDataBase(conn, 'select * from manifestation')
 
print("Bem-vindo a ouvidoria da Universidade XYZ, na qual sua voz é importante!")
seunome = input("Por favor, digite seu nome usuário: ")
print(f"Olá {seunome}, o que você gostaria de fazer?")

while option != 7:
    option = int(input("\n Selecione uma das opções abaixo: \n 1) 🔍 Listagem das Manifestações \n 2) 📂 Listagem das manifestações filtradas por tipo \n 3) ➕ Criar uma nova manifestação \n 4) 📊 Exibir a quantidade total de manifestações \n 5) 🔎 Pesquisar uma manifestação através do código \n 6) 🗑️  Excluir uma manifestação pelo código \n 7) 🚪 Sair do sistema \n" ))
    
    
    if option == 1:
        consultationListManifestations = "SELECT * FROM manifestation"
        manifestation = listDataBase(conn, consultationListManifestations)
        if len(manifestation) > 0:
            print("Aqui estão as manifestações cadastradas: \n")
            for manifest in manifestation:
                print(f"Código: {manifest[0]} - Tipo: {manifest[1]} - Manifestação: {manifest[2]}")
        else:
            print("Sem manifestações no sistema.")

    elif option == 2:
        print("Filtrar manifestações por tipo:")
        print("1) 😡 Reclamação \n2) 💡 Sugestão \n3) 🌟 Elogio")

        while True:
            tipo = input("Digite o número correspondente ao tipo desejado: ")
            if tipo in ["1", "2", "3"]:
                typeManifestation = {"1": "Reclamação", "2": "Sugestão", "3": "Elogio"}
                typeChoose = typeManifestation[tipo]
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")

        consulta = "SELECT * FROM manifestation WHERE tipo = %s"
        data = [typeChoose]
        manifestacoes_filtradas = listDataBase(conn, consulta, data)

        if len(manifestacoes_filtradas) > 0:
            print(f"Manifestações do tipo {typeChoose}:")
            for manifest in manifestacoes_filtradas:
                print(f"Código: {manifest[0]} - Manifestação: {manifest[2]}")
        else:
            print(f"Nenhuma manifestação do tipo {typeChoose} encontrada.")

    elif option == 3:
        print("Antes de cadastrar sua manifestação, escolha o tipo:")
        print("1) 😡 Reclamação \n2) 💡 Sugestão \n3) 🌟 Elogio")

        while True:
            tipo = input("Digite o número correspondente ao tipo da manifestação: ")
            if tipo in ["1", "2", "3"]:
                typeManifestation = {"1": "Reclamação", "2": "Sugestão", "3": "Elogio"}
                typeChoose = typeManifestation[tipo]
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")
        if tipo == "1":
                newManifestation = input("Por favor, digite a sua reclamação: ").strip()
        elif tipo == "2":
                newManifestation = input("Por favor, digite a sua sugestão: ").strip()
        elif tipo == "3":
                newManifestation = input("Por favor, digite o seu elogio: ").strip()
        while len(newManifestation) < 1:
                newManifestation = input("Manifestação inválida. Digite novamente: ").strip()

        insertConsultation = "INSERT INTO manifestation (tipo, manifestacao) VALUES (%s, %s)"
        data = [typeChoose, newManifestation]
        insertInDataBase(conn, insertConsultation, data)

        consultaID = "SELECT LAST_INSERT_ID()"
        position = listDataBase(conn, consultaID)[0][0]

        print(f"{typeChoose} cadastrada com sucesso! Seu código é: {position}")

    elif option == 4:
        consultationListManifestations = 'SELECT COUNT(*) FROM manifestation'
        resultado = listDataBase(conn, consultationListManifestations)
        manifestationQuantity = resultado[0][0]

        if manifestationQuantity > 0:
            print(f"Temos {manifestationQuantity} manifestações cadastradas no sistema.")
        else:
            print("Não há manifestações cadastradas no sistema.")

    
    elif option == 5:
        consultationListManifestations = "SELECT COUNT(*) FROM manifestation"
        resultado = listDataBase(conn, consultationListManifestations)
        quantidade = resultado[0][0]

        if quantidade == 0:
            print("Não há manifestações cadastradas no sistema.")
        else:
            while True:
                searchManifestation = int(input("Digite o código da manifestação que deseja encontrar: "))
                data = [searchManifestation]
                consultationSearch = "SELECT * FROM manifestation WHERE codigo = %s"
                manifestation = listDataBase(conn, consultationSearch, data)

                if len(manifestation) == 0 or searchManifestation < 1:
                    print("Manifestação não encontrada, tente novamente!")
                else:
                    print(f"Manifestação encontrada! \n{manifestation[0][1]}: {manifestation[0][2]}")
                    break

    elif option == 6:
        consultationListManifestations = "SELECT COUNT(*) FROM manifestation"
        resultado = listDataBase(conn, consultationListManifestations)
        quantidade = resultado[0][0]

        if quantidade == 0:
            print("Não há manifestações cadastradas no sistema.")
        else:
            while True:
                deleteManifestation = int(input("Digite o código da manifestação que deseja excluir: "))
                data = [deleteManifestation]
                consultationDelete = "SELECT * FROM manifestation WHERE codigo = %s"
                manifestation = listDataBase(conn, consultationDelete, data)
                
                if len(manifestation) == 0 or deleteManifestation < 1:
                    print("Manifestação não encontrada, tente novamente!")
                else:
                    deleteConsultation = "DELETE FROM manifestation WHERE codigo = %s"
                    deleteDataBase(conn, deleteConsultation, data)
                    print(f"Manifestação com o código {deleteManifestation} excluída com sucesso.")
                    break

    
    elif option == 7:
        print(f"Agradecemos pelo uso, {seunome}.")
    

    else:
        print("Opção inválida.")
