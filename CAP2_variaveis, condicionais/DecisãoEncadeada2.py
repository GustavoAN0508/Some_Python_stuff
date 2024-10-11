nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
doençaInfec = input ("tens alguma doença infecciosa? ").upper()
#acima de 65 prioridade
#se doente sala amarela, se não sala vermelha
#Agora vamos considerar grávidas também

#primeiro problema, tem ou não tem doença
if doençaInfec == "SIM":
    print("encaminhem-no a sala amarela")
elif doençaInfec == "NÃO":
    print("encaminhem-no a sala vermelha")
else:
    print("Deu ruim.")


#segundo problema, tem ou não tem prioridade
if idade >= 65:
    print("paciente",nome,"tem prioridade")
else:  
    genero = input("Qual seu gênero? ").upper()
    if genero == "FEMININO":
        gravida = input("Você é gestante? ").upper()
        if gravida == "SIM":
            print(nome,"é gestante, logo, tem prioridade")
        elif gravida =="NÃO":
            print (nome,"não é gestante, logo, cagamos para você")
        else:
            print("erro.")
    elif genero == "MASCULINO":
        print (nome,"não é muié cagamos para você")
    else:
        print("essa merda de não-binário, não existe.")
