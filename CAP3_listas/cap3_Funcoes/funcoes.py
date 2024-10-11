def prenchInventário (lista):
    resp = input ("Deseja continuar? (S/N)").upper()
    while resp == "S":
        equipamento = [input("Equipamento: \n"),
                       float(input("Valor: \n")),
                       int(input("Numero Serial: \n")),
                       input("Departamento: \n")]
        lista.append(equipamento)
        resp = input("Digite S para confimar: (S/N)").upper()

def exibirFunção(lista):
    for elemento in lista:
        print("Equipamento...:", elemento[0])
        print("Valor.........:", elemento[1])
        print("Numero Serial.:", elemento[2])
print("Departamento..:", elemento[3])
        
def localizarNome(lista):
    busca = input("Qual equipamento deseja buscar?")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor.......:", elemento[1])
            print("Serial......:", elemento[2])
            print("Departamento:", elemento[3])

def depreciarPorNome(lista,porc):
    depreciacao = input("Qual equipamento deseja depreciar?")
    for elemento in lista:
         if depreciacao == elemento[0]:
            print("Valor antigo:", elemento[1])
            elemento[1] = elemento[1]*(1-porc[1]/100)
            print("Novo valor:", elemento[1])
                
def excluirporSerial(lista):
    for elemento in lista:
        serial = int(input("Digite o serial do item que deseja excluit: "))
        if serial == elemento[2]:
            lista.remove(elemento)
    return "itens excluidos."

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
        if len(valores)>0:
            print("Valor mais alto: ", max(valores))
            print("Valor mais baixo: ", min(valores))
            print("Total: ", sum(valores))
