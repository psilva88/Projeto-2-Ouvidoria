from operacoesbd_english_cirugia import *

def opcao1(conn):
        consultationListManifestations = "select * from manifestation"
        manifestation = listDataBase(conn, consultationListManifestations)
        if len(manifestation) > 0:
            print("Aqui está as manifestações cadastradas: \n")
            for manifest in range(len(manifestation)):
                print(f"Código da Manifestação: {manifestation[manifest][0]} - {manifestation[manifest][1]}.")
        else:
            print("Sem manifestações no sistema.")

def opcao2(conn):
    print("Escolha o tipo de manifestação: \n1) 😡 Reclamação \n2) 💡 Sugestão \n3) 🌟 Elogio")

def opcao3(conn):
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

def opcao4(conn):
    consultationListManifestations = 'select count(*) from manifestation'
    resultado = listDataBase(conn, consultationListManifestations)
    manifestationQuantity = resultado[0][0]

    if manifestationQuantity > 0:
            print(f"Temos {manifestationQuantity} manifestações cadastradas no sistema.")
    else:
            print("Não há manifestações cadastradas no sistema.")

def opcao5(conn):
    while True:
            searchManifestation = int(input("Digite o código da manifestação que deseja encontrar: "))
            data = [ searchManifestation ]
            consultationSearch = "select * from manifestation where codigo = %s"
            manifestation = listDataBase(conn, consultationSearch, data)
            if len(manifestation) == 0 or searchManifestation < 1:
                searchManifestation = int(input("Manifestação não encontrada, tente novamente: "))
                print("Manifestação não encontrada, tente novamente!")
            else:
                print(f"Manifestação encontrada: -{manifestation [0][1]}")
                break

def opcao6(conn):
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

def opcao7(seunome):
    print(f"👋 Obrigado por usar a ouvidoria, {seunome}!")
