a = int(input("Coloca um número aí, por gentileza: "))

if(a % 2 != 0):
    for numero in range(1,a,1):
        if(a % numero != 0 and numero != 1):    
                print(f"{a} é número primo")
                break

            
        elif(a % numero == 0 and numero !=1):
            print(f"{a} não é primo")
            break
elif(a == 2):
    print(f"{a} é um número primo")

else:
    print(f"{a} não é primo")