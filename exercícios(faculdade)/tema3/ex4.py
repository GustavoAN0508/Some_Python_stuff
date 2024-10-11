num1 = int(input("Digite um numero dividendo: "))
num2 = int(input("Digite outro numero divisor: "))

if(num1 % num2 == 0):
    print(f"{num1} é multiplo de {num2}")
else:
    print(f"{num1} não é multiplo de {num2}")