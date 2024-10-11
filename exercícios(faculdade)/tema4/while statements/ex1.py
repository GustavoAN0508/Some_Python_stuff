n = 0
lista = []

while (n<9):
    lista.append(int(input("Insira um valor aqui: ")))
    lista.sort()
    
    n += 1

n=0
maior = lista[0]
menor = lista [0]
while(n < 8):
    if(lista[n+1] > lista[n]):
        maior = lista[n+1]
    
    n += 1

n = 0
while(n < 8):
    if(lista[n+1] < lista[n]):
        menor = lista[n+1]
    n += 1

n = 0
media = (maior+menor)/2

print("A lista de números é: ")
while (n < len(lista)):
    print(lista[n], end=" ")
    n += 1
print("\n\nO maior número da lista é: ", maior)
print("O menor número da lista é: " , menor)
print("A média entre maior e menor é: ", media)