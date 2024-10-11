a = int(input("Medida do primeiro segmento de reta: "))
b = int(input("Medida do segundo segmento de reta: "))
c = int(input("Medida do terceiro segmento de reta: "))

if (a < (b+c) and b < (a+c) and c < (a+b)):
    print(f"{a}, {b} e {c} são medidas possíveis para formar um triângulo\n\n\n")
    if(a == b and a == c and b == c):
        print(f"É um triângulo equilátero")
    elif((a == b and a !=c) or (a == c and a != b) or (b == c and b != a)):
        print(f"É um triângulo isósceles")
    elif( a != b and a != c):
        print(f"É um triângulo escaleno")
else:
    print(f"{a},{b} e {c} não são medidas possíveis para formar um triângulo \n\n\n")
