print("**"*10)
print("Trabalhando com Lista")
print("**"*10)
#lita1 = [1, 2, 3, 4, 5, 6, 8, 7, 9]
#print(lista1)

arquivo = open("pessoas.txt", "w")
print(arquivo)
arquivo.write("Silvio\n")
arquivo.write("Sérgio\n")
arquivo.write("Darkson\n")
arquivo.write("Severiano\n")
arquivo.write("Dadimar\n")
novo_arquivo = arquivo
novo_arquivo.write("Rayan")
novo_arquivo.write("Dafine")
arquivo.close()