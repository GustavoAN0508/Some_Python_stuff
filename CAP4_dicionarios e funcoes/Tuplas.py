ips = {} 
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("digite os dois últimos octetos: "))] = input("nome da máquina: ")
    resp = input("Digite S para continuar: ").upper()
    print("Exibindo endereços IP: ")
    for ip in ips.keys():
        print(ip[0]+"."+ip[1])
    print("Exibindo máquinas no mesmo endereço: ")
    pesquisa = input("digite os dois últimos octetos: ")
    for ip,nome in ips.items()
        if(ip[1]==pesquisa):
            print(nome)
    Print("Exibindo máquinas na mesma rede: ")
    rede=input("digite os dois primeiros octetos: ")
    for nome in ips.items()
        if (ip[0] == rede)
            print(nome)
