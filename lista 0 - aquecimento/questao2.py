A = "*"
altura = int(input("altura *:"))
qnt = int(input("quantidade de *:"))
if qnt > 20:
    print("não pode passar mais de 20")
else:
    print("\nretangulo:\n")
    for x in range(altura):
        for y in range(qnt):
            print(A, end=' ')
        print()
    
    print("\ndiagonal superior direito:\n")    
    for z in range(qnt, 0, -1):
        espaco = qnt - z
        print("  " * espaco + (A+" ")* z)
