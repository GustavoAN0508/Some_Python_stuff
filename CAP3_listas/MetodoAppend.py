inventário = []
resposta = "S"
while resposta == "S":
    inventário.append(input("Equipamento: "))
    inventário.append(float(input("Valor: ")))
    inventário.append(int(input("Numero serial: ")))
    inventário.append(input("Departamento: "))
    resposta = input("Responda S para continuar: ").upper

for elemento in inventário:
    print(elemento)
