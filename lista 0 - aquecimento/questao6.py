'''
Trava lógica – simulando o comportamento de uma fechadura eletrônica.
Para desenvolver este programa, tome como base a senha correta:1-2-3, onde, o
símbolo de menos é utilizado apenas como delimitador. O objetivo é determinar
se a senha está ou não correta, para isso considere o seguinte:
• Defina uma variável chamada estado, que possui valor inicial igual a zero.
• Faça a varredura dos caracteres e utilize o switch-case para determinar os
novos estados. Caso a entrada na posição 1 for 1, o estado vai para 1, caso
contrário, ele vai para zero. Lembre-se, os estados são dependentes. Se ao
final o valor da variável estado for três, imprima “Acesso concedido!”.
'''
# n tem switch-case em python, vou usar if/else

def Trava(senha):
    tentativa = senha.split('-')
    estado = 0
    for x in tentativa:
        if estado ==  0 and x == '1':       
            estado += 1
            #print(estado)     
        elif estado ==  1 and x == '2':
            estado += 1  
            #print(estado)                       
        elif estado == 2 and x == '3':
            estado += 1
            #print(estado)     
        else: 
            estado = 0
            break
    #print(estado)
    #print(tentativa)
    if estado == 3:
        print("Acesso Concedido!")
    else:
        print("Acesso Negado!")

senha = input("digita a senha(no formato ex:'1-2-3'): ")
Trava(senha)