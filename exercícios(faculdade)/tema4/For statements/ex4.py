lista = []
maior = 0
menor = 0

for a in range(0,9,1):
    lista.append(int(input("Coloque um número aqui: ")))
    lista.sort()

for b in range(0,len(lista),1):
    if (lista[b] > lista[b-1]):
        maior = lista[b]

for c in range(0, len(lista), 1):
    if (lista [c] < lista[c-1]):
        menor = lista[c]

media = (maior + menor)/2

print(f"o maior número é {maior}\n")
print(f"o menor número é {menor}\n")
print(f"a média entre esses números é {media}")