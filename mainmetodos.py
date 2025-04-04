from operacoesbd_english import *

def opcao1(conn):
        consultationListManifestations = "SELECT * FROM manifestation"
        manifestation = listDataBase(conn, consultationListManifestations)
        if len(manifestation) > 0:
            print("Aqui estão as manifestações cadastradas: \n")
            for manifest in manifestation:
                print(f"Código: {manifest[0]} - Tipo: {manifest[1]} - Manifestação: {manifest[2]}")
        else:
            print("Sem manifestações no sistema.")

def opcao2(conn):
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

def opcao3(conn):
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

        newManifestation = input("Por favor, digite a sua manifestação: ").strip()
        while len(newManifestation) < 1:
            newManifestation = input("Manifestação inválida. Digite novamente: ").strip()

        insertConsultation = "INSERT INTO manifestation (tipo, manifestacao) VALUES (%s, %s)"
        data = [typeChoose, newManifestation]
        insertInDataBase(conn, insertConsultation, data)

        consultaID = "SELECT LAST_INSERT_ID()"
        position = listDataBase(conn, consultaID)[0][0]

        print(f"{typeChoose} cadastrada com sucesso! Seu código é: {position}")

def opcao4(conn):
        consultationListManifestations = 'SELECT COUNT(*) FROM manifestation'
        resultado = listDataBase(conn, consultationListManifestations)
        manifestationQuantity = resultado[0][0]

        if manifestationQuantity > 0:
            print(f"Temos {manifestationQuantity} manifestações cadastradas no sistema.")
        else:
            print("Não há manifestações cadastradas no sistema.")

def opcao5(conn):
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

def opcao6(conn):
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

def opcao7(seunome):
    print(f"👋 Obrigado por usar a ouvidoria, {seunome}!")
