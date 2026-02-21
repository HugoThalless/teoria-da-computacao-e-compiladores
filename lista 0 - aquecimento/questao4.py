def token(txt):
    tokens = txt.split()
    for x in tokens:
        if x == "[a-zA-Z]":
            print(f"",x," -> Identificador")
        elif x == "=":
            print(f"",x," -> atribuição")
        elif x.isdigit():
            print(f"",x," -> Número")
        elif x in "+-*/":
            print(f"",x," -> Operador")
        elif x.isdigit():
            print(f"",x," -> Número")
        elif x == ";":
            print(f"",x," -> Fim de instrução")        

txt = "soma = 10 + 20 ;"
token(txt)