inventario = {}
opcao = int(input("digite: \n<1>registra ativo\n<2>persiste arquivo\n<3>exibe ativos armazenados"))

while opcao > 0 and opcao < 4:
    if opcao == 1:
        resp="S"
        while resp=="S":
            inventario[input("digite numero patrimonial: ")] = [
                input("digite a data da ultima atualização: "),
                input("digite a descrição: "),
                input("digite o departamento: ")
            ]
            resp = input("digite S para continuar").upper().strip()
    elif opcao == 2:
        with open ("inventario.csv","a") as inv:
            for chave, valor in inventario.itens():
                inv.write(f"chave:\n{valor[0]};{valor[1]};{valor[2]};{valor[3]}")
            print("persistido com sucesso.")
    elif opcao == 3:
        with open ("inventario.csv","r"):
            print(inv.readline())