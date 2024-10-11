import json
inventario = {}
opcao = int(input("1. para registrar ativo\n2.para exibir ativos armazenados\nDigite:"))
while opcao>0 and opcao<3:
    if opcao == 1:
        resp = 1
        while resp == 1:
            inventario[input("digite o numero patrimonial: ")] = [
                input("Digite a última data de atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")
            ]
            resp = int(input("Digite <1> para continuar").upper())
        with open("inventario_json.json","w") as arqJSON:
            json.dump(inventario, arqJSON)
        print("JSON gerado!!!")
        break
    elif opcao == 2:
        with open("inventario_json.json","r") as arqJSON:
            resultado = json.load(arqJSON)
            for chave, dado in resultado.items():
                print(f"Data...............:{dado[0]}")
                print(f"Descrição..........:{dado[1]}")
                print(f"Departamento.......:{dado[2]}")
            break
