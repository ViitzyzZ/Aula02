#Sintaxe de criação da tupla
minhaTupla = ("Açai", "Leite Ninho", "Nutella","tupla")
print("Mostrar a tupla: ",minhaTupla)
print("Mostrar um item em posição esopecífica: ",minhaTupla[2])
print("Mostrar o último item da tupla: ",minhaTupla[-1])
print("Mostrar um intervalo de itens: ",minhaTupla[1:2])

#tentando alterar item da tupla / OBS > em uma tupla não é possível alterar sem a "Lista Clandestina"
#minhaTupla[1] = "Leite em Pó"
#print(minhaTupla)

#Burlando alterações de dados na tupla
listaclandestina = list(minhaTupla)
print("Lista Clandestina: ", listaclandestina)
listaclandestina[2] = "Leite Condensado"
print("Lista Clandestina com dado alterado: ",listaclandestina)
minhaTupla = tuple(listaclandestina)
print("Minha tupla clandestina: ",minhaTupla)

#Criar a tupla com apenas um item("É OBRIGATÓRIO TER A VÍRGULA"(TEM QUE TER A VÍRGULA(,)))
minhaTuplaDois = ('tupla',)
print(type(minhaTuplaDois))
print("Acessando pela posição ordenada: ",minhaTuplaDois[0])
print("Acessando indexação negativa: ",minhaTuplaDois[-1])

#Excluir a tupla completamente
#del minhaTuplaDois
#print("Tentando: ",minhaTuplaDois)

#Juntando tuplas
minhaTuplaTres = minhaTupla + minhaTuplaDois
print("Juntando tuplas: ",minhaTuplaTres)

#A função count() serve para contar as vezes que se repete
quantidadeQueRepete = minhaTuplaTres.count('tupla')
print("Usando função count: ",quantidadeQueRepete)

#A função index() serve para retornar primeira ocorrência do item
posicaoDoItem = minhaTuplaTres.index('tupla')
print("Usando função index(Retorna primeira posição): ",posicaoDoItem)