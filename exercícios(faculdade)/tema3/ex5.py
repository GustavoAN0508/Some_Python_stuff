a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
array = []

if(a > b and a > c):
    array.append(a)
    if(b>c):
        array.append(b)
        array.append(c)
    else:
        array.append(c)
        array.append(b)

elif(a>b and a<c):
    array.append(c)
    array.append(a)
    array.append(b)

elif(a<b and a>c):
    array.append(b)
    array.append(a)
    array.append(c)
else:
    if(b>c):
        array.append(b)
        array.append(c)
    else:
        array.append(c)
        array.append(b)
    array.append(a)

print(f"O maior número da lista é {array[0]}\nO menor número da lista é {array[2]}")

