#Sintaxe de uma lista(array) em python
minhaLista = ["Eduardo", "Julia", "Ana",10]
print(minhaLista)

#Acesso ao item por posição
print("Acesso por posição: ",minhaLista[0])

#Acesso indexado negativo por posição
print("Acesso indexado negativo: ",minhaLista[-1])

#Intervalo de itens
print("Intervalo de itens: ",minhaLista[1:3])
print("Intervalo de itens sem o item de início: ",minhaLista[:2])
print("Intervalo de itens sem o item de final : ",minhaLista[1:])

#Intervalo de itens indexação negativo
print("Intervalo de itens: ",minhaLista[-2:-1])

#Alterando valor do item
minhaLista[3] = "Francine"
print("Lista com valor do item alterado: ",minhaLista)

#Percorrer lista
for i in minhaLista:
    print("Item da lista:c",i)

if "Julia" in minhaLista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")

#Retorna quantidade de itens na lista
print("Quantidade de itens na lista: ", len(minhaLista))

minhaLista.append("Henrique")
print("Minha lista com novo item no final: ",minhaLista)

#Adiciona item na posição escolhida
minhaLista.insert(1,"Madu")
print("Minha lista com item em posição específica: ",minhaLista)

#Remover item específico
minhaLista.remove("Francine")
print("Minha lista com item removido: ",minhaLista)

#Remove o índice específicado
minhaLista.pop(4)
print("Minha lista com índice removido: ",minhaLista)

minhaLista.pop()
print("Minha lista com índice removido: ",minhaLista)

del minhaLista[1]
print("Minha lista com item removido com del ",minhaLista)

#Deleta a lista toda APAGA TUDO!
#del minhalista

#Limpa a lista mas não deleta ela.
minhaLista.clear()
print("Minha lista vazia com o método clear ",minhaLista)

minhaLista.insert(0, "hello")
minhaLista.insert(1, "opa")
print("Minha lista com novos itens ",minhaLista)
#Copia dados de uma lista para a outra lista
minhaSegundaLista = minhaLista.copy()
print("Lista que copiou a outra (coisa de alunos)",minhaSegundaLista)
#Copia dados de uma lista para a outra lista
minhaTerceiraLista = list(minhaSegundaLista)
print("Lista que copiou a outra (coisa de alunos)",minhaTerceiraLista)

minhaSegundaLista.append("eae")
minhaTerceiraLista.insert(0, "hello")

print("Adicionando novos amiguinhos na segunda lista", minhaSegundaLista)
print("Adicionando novos amiguinhos na terceira lista", minhaTerceiraLista)

print("Quantidade de vezes que repete hello: ", minhaTerceiraLista.count("hello"))
#Juntando listas
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print("Juntando listas ", minhaQuartaLista)
#Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ", minhaQuartaLista.index("eae"))
