ainventario = []
resposta = "S"
while resposta == "S":
    equipamento = [input("equipamentos: "),
                   float(input("valor:")),
                   int(input("numeroSerial: ")),
                   input("departamento: ")]
    inventario.append(equipamento)
    resposta = input("digite S para continuar: ").upper()

for elemento in inventario:
    print("nome.........: ", elemento[0])
    print("valor........: ", elemento[1])
    print("numero serial: ", elemento[2])
    print("departamento.: ", elemento[3])
        
busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("valor.: ", elemento[1])
        print("serial: ", elemento[2])
    
depreciacao = input("digite o nome do equipamento a ser depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
     print("valor antigo:", elemento[1])
     elemento[1] = elemento[1]*0,9
     print("novo valor: ", elemento[1])
     
serial = int(input("Digite o serial que será excluido: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)
    
for elemento in inventario:
        print("nome.........: ", elemento[0])
        print("valor........: ", elemento[1])
        print("numero serial: ", elemento[2])
        print("departamento.: ", elemento[3])

valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))
