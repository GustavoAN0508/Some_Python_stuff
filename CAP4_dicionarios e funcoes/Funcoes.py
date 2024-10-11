def pergunta():
    resposta = input("Bem vindo ao sistema!\n"+"<I> para inserção de usuários\n"+"<P> para pesquisa de usuário\n"+"<E> para exclusão de usuário\n"+"<L> para listar usuário").upper()
return resposta

def inserir (dicionario):
    dicionario[input("digite o login: ")]= [
        input("digite o nome: ").upper(),
        input("digite a data: "),
        input("digite a estação: ").upper()
    ]
