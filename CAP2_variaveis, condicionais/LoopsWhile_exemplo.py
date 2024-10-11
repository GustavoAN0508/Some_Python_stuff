resposta = "SIM"

while resposta == "SIM":
    tipo = input("Você é ADM, USR ou GUEST?").upper()
    if tipo == "ADM":
        genero = input("Qual seu gênero?").upper()
        if genero == "FEMININO":
            print("Olá, administradora.")
        else:
            print("Olá, ademir corno.")
    elif tipo == "ADM" or "USR":
        genero = input("Qual seu gênero?").upper()
        if genero == "FEMININO":
            print("Olá, usuária.")
        else:
            print("Olá, usuário.")
    elif tipo == "GUEST":
            print("Olá, visitante.")
    else:
        print("Erro.")
    resposta = input("digite sim para continuar: ").upper()
