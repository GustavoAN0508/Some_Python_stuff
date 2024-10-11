form = int(input("Digite um número inteiro aqui; "))
div = []

for item in range(1, form, 1):
    if (form % item == 0 ):
        div.append(item)
    

print(div)