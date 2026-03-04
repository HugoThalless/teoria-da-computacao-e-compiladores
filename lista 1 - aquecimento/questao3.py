RH = {"ver_salario", "editar_perfil"} 
TI = {"acesso_servidor", "editar_perfil"}
total_permicoes = {RH | TI}
acesso = {'acesso_servidor', 'ver_salario', 'editar_perfil'}

print(f"conjunto total de permições com os 2 cargos:{total_permicoes}")
if total_permicoes >= acesso:
    print("Acesso concedido ao arquivo")
else:  print("acesso negado")

