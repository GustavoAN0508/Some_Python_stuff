usuarios={} #Indica que foi criado um dicionário
usuarios={
    #chave  #informações contidas na chave
    chaves:["Silva", "24/09/2021", "recep_01"],
    quico:["Enrico Flores", "13/08/2017", "raiox_02"],
    quico:["Enrico Flores", "14/08/2018","raiox_02"] #essa chave quico irá sobrescrever a de cima'
}
#há essa forma de escrever uma chave em um dicionario
usuarios["florinda"]=["Flores","17/09/2016", "recep_01"]
usuarios["florinda"]=["Flores","1709/2017","recep_02"] #da mesma forma, essa sobrescreve as informações acima

print(usuarios) #aqui, printa-se todas as chaves e suas informações
print("###################")
print("Dados: "usuarios.get("chaves")) #O get() irá pegar as informações contidas em "chaves"
