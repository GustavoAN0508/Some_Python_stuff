from cap3_Funcoes.funcoes import*

lista = []
print("preenchendo")
prenchInventario(lista)
print("exibindo")
exibirFuncao(lista)

print("pesquisando")
localizarPorNome(lista)
print("alterando")
depreciarPorNome(lista, 20)

print("excluindo")
print(excluirporSerial(lista))
exibirFuncao(lista)

print("Resumindo")
resumirValores(lista)

