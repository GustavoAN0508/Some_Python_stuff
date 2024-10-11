L = int(input("Digite quantos asterísticos terá o lado do seu quadrado de asterísticos: "))

for a in range(0,L,1):
    if(a == 0 or a == L-1):
        print("*"*L)     
    else:
        print("*"+" "*(L-2)+"*")