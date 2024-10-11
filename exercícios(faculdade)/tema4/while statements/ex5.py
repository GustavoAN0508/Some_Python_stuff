palavra = str(input("Coloque uma palavra aqui: "))
letras = list(palavra)
a = 0

while(a < len(letras)):
    print(letras[a], end=" ")
    a += 1

print("\na palavra tem",len(letras),"letras")