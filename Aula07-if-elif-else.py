#Operadores lógicos que podemos usar com if.
#a==b  igual
#a!=b  diferente
#a<b   menor      a=1 b=2 / 12345 b=6 
#a<=b  menor igual          123456 b=6
#a>b   maior      a=3 b=7 false
#a>=b  maior igual

a=2
b=4
c=2

#IF
if a<b:
    print("Sim é menor")
    c=a
    print("Valor de c",c)
elif a==b:
    print("Sim é igual")
else:
    print("Dado não identificado!")

#If com uso de um operador lógico, alinhamento(if dentro de if).
if a<b:
    print("Sim é menor")
    c=a
    print("Valor de c",c)
    if c==b:
        print("Sim é igual")
    else:
        print("Não é!")
else:
    print("Não é menor")

#If ternário ou operador ternário, se dentro do bloco do if tiver apenas uma linha.
if a<b: print("É menor!")

#If eles ternário ou operadores ternários, se dentro do bloco do if tiver apenas uma linha.
print("b é maior") if a < b else print("o b não é maior")

#If para fazer masi de uma verificação.
if a < b and c!=a:
    print("Valor de a: ",a)
    print("Valor de b: ",b)
    print("Valor de c: ",c)
    print("(And) Isso é verdade!", c)
elif a<b or c!=a:
    print("(or) Isso é verdade!")

#Não podemos criar if, elif ou else vazio, se precisar criar assim, use o pass.
if a<b:
    pass


