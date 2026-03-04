RESERVADAS = {"if", "else", "while",
"for", "return", "int", "System", "out", "print", "public",
"class", "println"}

txt = '''
public class StarRectangle {
	public void printRectangle(int n) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(" * ");
			}
			System.out.println();
		}
	}	
	public void printBottonLeftTriangle(int n) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				System.out.print(" * ");
			}
			System.out.println();
		}
	}
	public void printTopRightTriangle(int n) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (j < i){
					System.out.print(" ");
				}else{
					System.out.print(" * ");
				}
			}
			System.out.println();
		}
	}
}
'''
separador = (".", "(", ")", "{", ";")

for  x in separador:
    txt = txt.replace(x, f" {x} ")

intersecao = {}
diferenca = {}
tokens = set(txt.split())

intersecao = tokens & RESERVADAS
diferenca = tokens - RESERVADAS 
print(tokens,"\n")
print(f"interseção:{intersecao}\n")
print(f"diferença:{diferenca}\n")