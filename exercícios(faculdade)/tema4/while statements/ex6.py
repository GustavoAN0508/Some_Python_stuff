nota1 = float(input("Coloque aqui o valor da primeira nota: "))
nota2 = float(input("Coloque aqui o valor da segunda nota: "))

media = (nota1 + nota2)/2

if (media >= 6):
    print("Aprovado, some daqui!")

elif(media >= 4 and media < 6):
    print("Ainda tem chance, vamos! Exame final!")
    
else:
    print("Reprovado!!!!!! *slams the desk*")
