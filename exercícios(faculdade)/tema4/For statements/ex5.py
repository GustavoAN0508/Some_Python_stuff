n = int(input("Coloque um número inteiro aqui: "))
lista = []
fibbonaci = [1,2]
# fibbonaci = lista[x-1] + lista[x-2]

for a in range(0, n-2, 1):
    lista.append(a)
    if(lista[a-1] and lista[a-2]):
        fibbonaci.append(lista[a-1] + lista[a-2])
print(fibbonaci)