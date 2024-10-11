nome = input("Coloque seu nome aqui: ")
idade = input("Coloque sua idade aqui: ")
tem_Doença = input("Possui alguma doença infectocontagiosa? ").upper() #upper deixa tudo em maíusculo
if idade >= 65: #relação de se algo acontece então isso vai acontecer
    print("Você",nome,"tem prioridade")
elif tem_Doença == "SIM": # se então com dependência no If anterior, repare também que == é diferente de = pois um é matemático e outro é para definir variável
    print("O paciente",nome,"deve correr para o hospital!")
else: #Negação de todos os anteriores
    print(nome,"não tem prioridade")
