print("**"*10)
print("Busca nome")
print("**"*10)

nome = "Camila"

for palavra in nome:
    nome_digitado = input("Qual o nome: ").upper()
    index = 0
    if(nome_digitado == nome):
        print("A letra digitada foi {}".format(nome_digitado))
        print("O nome da Deusa do Egito da Africa do Sul é {}".format(nome))

        print(teste)
    index = index + 1
teste = palavra.find(nome_digitado)
