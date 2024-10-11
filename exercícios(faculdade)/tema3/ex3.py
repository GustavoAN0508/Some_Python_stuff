nome = str(input("Digite seu nome: "))
nota1 =  float(input("Digite sua nota: "))
nota2 = float(input("Digite sua outra nota: "))
media = (nota1 + nota2)/2

if (media >= 7):
    print(f"O aluno {nome} com suas notas {nota1} e {nota2} está aprovado!")
elif(media < 4):
    print(f"O aluno {nome} com suas notas {nota1} e {nota2} está reprovado!")
else:
    print(f"O aluno {nome} terá de fazer as provas finais, têm chance de passar.")