Usuario_A = {"Python", "Jogos", "Música", "IA"} 
Usuario_B = {"Java", "IA", "Música", "Caminhada"}
interesses = Usuario_A & Usuario_B
recomendacao = Usuario_B - Usuario_A
print(f"interesses em comum: {interesses}")
print(f"recomendação: {recomendacao}")

