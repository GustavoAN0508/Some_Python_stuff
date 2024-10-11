n = int(input("Coloque um número qualquer: "))

for a in range(0, n, 1):
    if(a % 2 != 0):
        for b in range(0, n, 1):
            print("*", end=" ")
        print(end="\n")
    
    else:
        for c in range(0, n, 1):
            print(" ", end="*")
        print(end="\n")