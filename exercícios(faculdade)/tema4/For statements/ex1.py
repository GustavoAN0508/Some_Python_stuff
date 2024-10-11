n = int(input("digite um número inteiro e par aqui: "))

if (n % 2 == 0):
    for numero in range(1, n, 2):
        if(numero % 2 != 0):
            print(numero, end=" ")
    print(n)

else:
    print("Era para ser um número par. \nEUVÔTEPEGAR >:(")