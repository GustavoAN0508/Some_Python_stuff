numero = int(input("Coloque o número de valores que você quer que tenha a lista: "))
a = 0
lista = []

while (a < numero):
    lista.append(int(input("Coloque um valor aqui: ")))
    a += 1

a = 0
maior = lista[0]
menor = lista[0]

while (a < len(lista)-1):
    if (lista[a+1] > lista[a]):
        maior = lista[a+1]
    a += 1
a=0


while (a < len(lista)-1):
    if (lista[a+1] < lista[a]):
        menor = lista[a+1]
    a+=1

print(lista)
print(maior)
print(menor)


