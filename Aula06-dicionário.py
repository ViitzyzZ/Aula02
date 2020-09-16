#Sintaxe do dicionário
#Chave: Valor
meuDicionario = {
    "nome": "Francine",
    "idade": 26
}
print("Mostrando o dicionário: ", meuDicionario)

#Acessando valor pela chave
print("Mostrando valor pela chave: ", meuDicionario['nome'])

#Acessando valor pelo método get()
print("Mostrando valor pela chave usando get(): ", meuDicionario.get('idade'))

#Alterando valor de um item específico
meuDicionario["nome"] = "Fran"
print("Novo valor da chave nome: ", meuDicionario["nome"])

#Percorrendo um dicionário para retornar as chaves
for x in meuDicionario:
    print("Percorrendo o dicionário para retornar chaves: ", x)

#Percorrendo um dicionário para retornar os valores
for x in meuDicionario:
    print("Percorrendo o dicionário para retornar o valor: ", meuDicionario[x])

#Percorrendo um dicionário para retornar o valor com values()
for x in meuDicionario.values():
    print("Percorrendo o dicionário para retornar o valor com values(): ", x)

#Percorrendo dicionário, mostrando chave e valor
for x in meuDicionario:
    print(x, meuDicionario[x])

#Verificar se a chave existe no dicionário
if "idade" in meuDicionario:
    print("Sim tem a chave idade no dicionário")

print("Tamanho do dicionário",len(meuDicionario))

#Adicionando novo item no dicionário
meuDicionario["cpf"] = "90987216572"
print("Adicionando novo item: (chave e valor): ",meuDicionario)

meuDicionario.pop("cpf")
print("Removendo item com função pop(): ", meuDicionario)

del meuDicionario["idade"]
print("Deletando item pela chave usando del: ", meuDicionario)

