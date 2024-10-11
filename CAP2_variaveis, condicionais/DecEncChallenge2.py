nome = input("seu nome aqui: ")
idade = int(input("sua idade aqui: "))
DoençaInfec = input("possui doença infectocontagiante? ").upper()

while DoençaInfec != "SIM" and DoençaInfec != "NÃO":
    print("digite sim ou não, burrão.")
    DoençaInfec = input("De novo, você tem ou não?").upper()

if DoençaInfec == "SIM":
    print("Você vai morrer antes do natal. SALA AMARELA!!!")

else:
    print("Tá salvo então, tenha um bom dia. SALA VERMELHA!!!")

if idade >= 65:
    print("paciente tem prioridade")
else:
    genero = input("qual seu gênero? ").upper()
    if genero == "MASCULINO":
        print(nome,"sem prioridade")
    elif gênero == "FEMININO":
        gravidez = input("És uma gestante? ")
        if gravidez == "SIM":
            print(nome,"é gestante e tem prioridade")
        elif gravidez == "NÃO":
            print(nome,"não tem prioridade")
        else:
            print("é sim ou não.")
    else:
        print("Isso não existe")
