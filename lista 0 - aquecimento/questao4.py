txt = "soma = 10 + 20 ;"
tokens = txt.split()
for x in tokens:
    if x.isidentifier():
        print(f"",x," -> Identificador")
    elif x == "=":
        print(f"",x," -> atribuição")
    elif x.isdigit():
        print(f"",x," -> Número")
    elif x in "+-*/":
        print(f"",x," -> Operador")
    elif x == ";":
        print(f"",x," -> Fim de instrução")       