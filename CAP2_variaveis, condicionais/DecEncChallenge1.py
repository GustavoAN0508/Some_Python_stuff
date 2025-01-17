nivel = input("Qual o seu nível na empresa?").upper()

if nivel == "ADM":
    genero = input("Você é homem ou mulher? ").upper()
    if genero == "MULHER":
        print ("Olá. administradora!")
    elif genero == "HOMEM":
        print("Olá, administrador!")
    else:
        print("Erro")
elif nivel == "USR":
    genero = input("Você é homem ou mulher? ").upper()
    if genero == "MULHER":
        print ("Olá. usuária!")
    elif genero == "HOMEM":
        print("Olá, usuário!")
    else:
        print("Erro")
elif nivel == "GUEST":
    genero = input("Você é homem ou mulher? ").upper()
    if genero == "MULHER":
        print ("Olá. convidada!")
    elif genero == "HOMEM":
        print("Olá, convidado!")
    else:
        print("Erro")
else:
    print("erro.")
