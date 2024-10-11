nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "não"
if idade > 65:
    prioridade = "sim"

print("O paciente", nome ,"possui atendimento prioritário?", prioridade)
