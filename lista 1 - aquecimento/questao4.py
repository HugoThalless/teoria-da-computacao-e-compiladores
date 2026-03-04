alfabeto = set("abcdefghijklmnopqrstuvwxyz")
print(f"alfabeto: {alfabeto}")
def validador(txt):
    letras_txt = set(txt.replace(" ", ""))
    print(letras_txt)
    if letras_txt - alfabeto == set():
        return print("todos os caracteres da frase pertencem ao alfabeto")
    else:
        return print("invalido:",letras_txt - alfabeto)    
    
txt = "o rato roeu a roupa do rei de roma"
validador(txt)