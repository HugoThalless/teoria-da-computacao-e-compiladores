A = "*"
qnt = int(input("quantidade de *:"))
if qnt > 20:
    print("não pode passar mais de 20")
else:
    for x in range(qnt):
        print((A+" ")*(x+1))