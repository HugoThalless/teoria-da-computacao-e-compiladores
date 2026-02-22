def verificador(expressao):
    stack = []
    pares = {")": "(","]": "[","}": "{"}

    for x in expressao:
        #print("o que tem no stack:",stack)
        #print("caractere: ",x,"\n")
        if x in "([{":
            #print("tem!")
            stack.append(x)
        elif x in ")]}":
            #print("tem2!")
            #print("peek stack:",stack[-1])
            if not stack:
                print("não tem abertura para um delimitador, expressão invalida")
                return
            elif stack[-1] == pares[x]:
                stack.pop()
                #print("removido,",stack)
            else:
                print("um o delimitador não esta fechado corretamente , expressão invalida")
                return
        #else:
        #    print("não é delimitador")

    if not stack:
        print("espressão esta fechados na ordem correta!")
    else:
        print("expressão invalida, delimitadores não fechado corretamente: ", stack)

#texto = "(a + [b ∗ c] − {d/e})"
texto = input("escreva a espressão para verificar: ")
verificador(texto)
