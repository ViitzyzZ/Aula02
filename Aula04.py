numeroA = 2
numeroB = 3

#Operadores aritiméticos

#soma
respostaSoma = numeroA + numeroB
print("resposta da soma:", respostaSoma)
print("resposta da soma:", (numeroA + numeroB))

#subtração
respostaSubtracao = numeroA - numeroB
print("resposta da subtração:", respostaSubtracao)
print("resposta da subtração:", (numeroA - numeroB))

#Multiplicação
respostaMultiplicacao = numeroA * numeroB
print("resposta da multiplicação:", respostaMultiplicacao)
print("resposta da multiplicação:",(numeroA * numeroB))

#preguiça
 #meuTexto = "resposta da multiplicação"
 #print(meuTexto, (numeroA * numeroB))

#Divisão
respostaDivisao = numeroA / numeroB
print("resposta da divisão:", respostaDivisao)
print("resposta da divisão:", (numeroA / numeroB))

#Expoente
respostaExpoente = numeroA ** numeroB
print("resposta do expoente:", respostaExpoente)
print("resposta do expoente:", (numeroA ** numeroB))

#Operadores lógicos e Relacionais
print("Operador lógico AND(e)", numeroA < 5 and numeroB < 10)
print("Operador lógico OR(ou)", (numeroA < 5 or numeroB > 20))
print("Operador lógico de NEGAÇÃO NOT(não)", (not(numeroA < 5 and numeroB < 10)))
print("Operador relacional != (diferente) : ", (numeroA != numeroB))

#Usando input para ler do teclado dado do tipo string (str)
armazenaValorTecladoString = input("Digite um texto: ")
print("O tipo do dado:", type(armazenaValorTecladoString))
print("O texto digitado:", armazenaValorTecladoString)

armazenaValorTecladoInt = int(input("Digite um valor inteiro: "))
print("O tipo do dado: ", type(armazenaValorTecladoInt))
print("O valor inteiro é: ", armazenaValorTecladoInt)

armazenaValorTecladoFloat = float(input("Digite um valor real: (Ex: 2.50)"))
print("O tipo do dado:", type(armazenaValorTecladoFloat))
print("O valor float é:", armazenaValorTecladoFloat)
