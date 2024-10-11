numero = int(input("Quantas vezes deseja converter para Celsius: "))
a = 0
while (a < numero):
    farenheit = float(input("Coloque um número aí para converter: "))
    celsius = (farenheit - 32)/1.8

    print("O número que você solicitou é:",celsius)

    a += 1



