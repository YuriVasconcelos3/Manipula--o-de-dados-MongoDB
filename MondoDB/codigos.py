from pymongo import MongoClient

client = MongoClient("localhost", 27017)

print(client.list_database_names())

db = client.Eletronica

def iniciar():
    db.Capacitores.insert_many([
    {"id":1, "tipo": "Capacitor Eletrolítico", "Capacitância": "2mF", "Quantidade": 34, "local": "Setor 1, gaveta 1"}, 
    {"id":2, "tipo": "Capacitor de Poliéster", "Capacitância": "1mF", "Quantidade": 41, "local": "Setor 1, gaveta 2"},
    {"id":3, "tipo": "Capacitor de tântalo", "Capacitância": "1.5mF", "Quantidade": 85, "local": "Setor 1, gaveta 3"}
    ])

    db.Resistencia.insert_many([
        {"id":1, "tipo": "Resistência de imersão", "Resistência": "0,05Ohm", "Quantidade": 33, "local": "Setor 2, gaveta 1"}, 
        {"id":2, "tipo": "Resistência tubular aletada", "Resistência": "0,04Ohm", "Quantidade": 52, "local": "Setor 2, gaveta 2"},
        {"id":3, "tipo": "Resistência cartucho", "Resistência": "0,06Ohm", "Quantidade": 55, "local": "Setor 2, gaveta 3"},
        {"id":4, "tipo": "Resistência flangeada", "Resistência": "0,05Ohm", "Quantidade": 66, "local": "Setor 2, gaveta 4"}

    ])

    db.Transistores.insert_many([
        {"id":1, "tipo": "TRANSISTOR BIPOLAR DE JUNÇÃO","Tensão": "0V-14V", "Quantidade": 14, "local": "Setor 3, gaveta 1"}, 
        {"id":2, "tipo": "TRANSISTOR DE EFEITO DE CAMPO","Tensão": "15V-35V", "Quantidade": 11, "local": "Setor 3, gaveta 2"},
        {"id":3, "tipo": "TRANSISTOR BIPOLAR DE GATE ISOLADO", "Tensão": "0V-500V", "Quantidade": 18, "local": "Setor 3, gaveta 3"}
    ])

    db.Microcontroladores.insert_many([
        {"id":1, "tipo": "ADK", "Memoria": "1Gb", "Quantidade": 14, "local": "Setor 4, gaveta 1"}, 
        {"id":2, "tipo": "Arduino", "Memoria": "3Gb", "Quantidade": 11, "local": "Setor 4, gaveta 2"},
        {"id":3, "tipo": "Raspberry Pi", "Memoria": "4Gb", "Quantidade": 18, "local": "Setor 4, gaveta 3"}
    ])

    db.Equipamentos.insert_many([
        {"id":1, "tipo": "Alicate", "Quantidade": 4, "local": "Setor 5, gaveta 1"}, 
        {"id":2, "tipo": "Ferro de solda", "Quantidade": 11, "local": "Setor 5, gaveta 2"},
        {"id":3, "tipo": "Solda", "Quantidade": 18, "local": "Setor 5, gaveta 3"},
        {"id":4, "tipo": "Soprador", "Quantidade": 8, "local": "Setor 5, gaveta 3"}
    ])

    


def menu():
    print('=====Gerenciador de registros=====')
    print('Selecione uma opção abaixo:')
    print('1- Inserir')
    print('2- Listar')
    opcao = int(input("Defina a opção: "))
    if opcao in [1, 2]:
        if opcao == 1:
            print('0- Inserir Capacitor')
            print('1- Inserir Resistência')
            print('2- Inserir Transistor')
            print('3- Inserir Microcontrolador')
            print('4- Inserir Equipamentos')
            opcao = int(input('Defina a OPÇÃO:'))
            if opcao in [0, 1, 2, 3, 4,5]:
                if opcao == 0:
                    id = int(input("Digite um ID: "))
                    tipo= str(input("Digite um tipo: "))
                    capacitancia = float(input("Digite a capacitancia: "))
                    quantidade = int(input("Digite a quantidade: "))
                    local = str(input("Digite o setor e gaveta: "))
                    db.Capacitores.insert_many([{ "id": id, "tipo": tipo, "capacitância": capacitancia, "quantidade": quantidade, "local": local }])
                elif opcao == 1:
                    id = int(input("Digite um ID: "))
                    tipo= str(input("Digite um tipo: "))
                    resistencia = float(input("Digite a resistencia: "))
                    quantidade = int(input("Digite a quantidade: "))
                    local = str(input("Digite o setor e gaveta: "))
                    db.Resistencia.insert_many([{"id":id, "tipo": tipo, "capacitância": resistencia, "quantidade": quantidade, "local": local }])
                elif opcao == 2:
                    id = int(input("Digite um ID: "))
                    tipo= str(input("Digite um tipo: "))
                    tensao = int(input("Digite a tensão: "))
                    quantidade = int(input("Digite a quantidade: "))
                    local = str(input("Digite o setor e gaveta: "))
                    db.transistores.insert_many([{"id":id, "tipo": tipo, "tensao": tensao, "quantidade": quantidade, "local": local }])
                elif opcao == 3:
                    id = int(input("Digite um ID: "))
                    tipo= str(input("Digite um tipo: "))
                    memoria = int(input("Digite a memória: "))
                    Quantidade = int(input("Digite a Quantidade: "))
                    local = str(input("Digite o setor e gaveta: "))
                    db.Microcontroladores.insert_many([{"id":id, "tipo": tipo, "Memória": memoria, "Quantidade": Quantidade, "local": local }])
                elif opcao == 4:
                    id = int(input("Digite um ID: "))
                    tipo= str(input("Digite um tipo: "))
                    Quantidade = int(input("Digite a Quantidade: "))
                    local = str(input("Digite o setor e gaveta: "))
                    db.Equipamentos.insert_many([{"id":id, "tipo": tipo, "capacitância": capacitancia, "Quantidade": Quantidade, "local": local }])
            else:
                print('Opcao invalida')
        elif opcao == 2:
            query = db.Capacitores.find()
            for n in query:
                print(n)