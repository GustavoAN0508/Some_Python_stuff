equipamentos = []
valor = []
numeroSerial = []
departamento = []
resposta="S"
while resposta=="S":
  equipamentos.append(input("Equipamento: "))
  valor.append(float(input("Valor: ")))
  numeroSerial.append(int(input("Número Serial: ")))
  departamento.append(input("Departamento: "))
  resposta=input("Digite S para continuar: ").upper()

for elemento in equipamentos:
    print("Equipamento:",elemento)

for elemento in valor:
    print("Valor: ",elemento)

for elemento in numeroSerial:
    print("numeroSerial: ",elemento)

for elemento in departamento:
    print("Departamento: ",elemento)
