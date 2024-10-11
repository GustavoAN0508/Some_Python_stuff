notas = [200.00 , 100.00 , 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
valor = float(input("Defina um valor a ser sacado: "))
print("Precisará de ")

if(valor % notas[0] == 0):
    print(f"{valor/notas[0]} notas de R${notas[0]},\n")

elif(valor % notas[1] == 0):
    print(f"{valor/notas[1]} notas de R${notas[1]},\n")

elif(valor % notas[2] == 0):
    print(f"{valor/notas[2]} notas de R${notas[2]},\n")

elif(valor % notas[3] == 0):
    print(f"{valor/notas[3]} notas de R${notas[3]},\n")

elif(valor % notas[4] == 0):
    print(f"{valor/notas[4]} notas de R${notas[4]},\n")

elif(valor % notas[5] == 0):
    print(f"{valor/notas[5]} notas de R${notas[5]},\n")

elif(valor % notas[6] == 0):
    print(f"{valor/notas[6]} notas de R${notas[6]},\n")

elif(valor % notas[7] == 0):
    print(f"{valor/notas[7]} notas de R${notas[7]}.")
