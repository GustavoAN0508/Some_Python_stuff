nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
doençaInfec = input ("tens alguma doença infecciosa? ").upper()
#acima de 65 prioridade
#se doente sala amarela, se não sala vermelha

if idade >= 65:
    print(nome," tem prioridade")
    if doençaInfec == "SIM":
        print("encaminhem-no para a sala amarela!")
    elif doençaInfec == "NÃO":
        print("encaminhem-no para a sala vermelha!")
    else:
        print("erro.")
else:
    print(nome," não tem prioridade")
    if doençaInfec == "SIM":
        print("encaminhem-no para a sala amarela")
    elif doençaInfec == "NÃO":
        print("encaminhem-no para a sala vermelha")
    else:
        print("deu ruim :(")
