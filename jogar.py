import random
def jogar():
    print("***"*10)
    print("Bem vindo ao jogo da Forca")
    print("***"*10)

    arquivo = open("frutas.txt","r")
    lista_palavra = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavra.append(linha)
    arquivo.close

    print( lista_palavra )

    numero = random.randrange(0, len(lista_palavra))

    palavra_secreta = lista_palavra[numero].upper()

    #palavra_secreta = "marca".upper()
    #Lop através de uma lista para percorrer a palavra secreta.
    letras_acertadas = ["_" for letra in palavra_secreta]

    print("Qual o nome da deusa do egito da africa do sul?")
    print( letras_acertadas )

    enforcou = False

    acertou = False
    erros = 0

    #Loop para verificar se o usuário não enforcou e não acertou
    while(not enforcou and not acertou):
        chute = input("Qual letra: ").strip().upper()
        #chute = chute

        #Fazendo uma busca pela letra
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if ( chute == letra ):
                   # print(letra)
                   #print("Encontrado a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
        enforcou = erros == 6 #False
        acertou = "_" not in letras_acertadas # verifica se a palavra secreta está preenchida.

    if (acertou):
        print("Você ganhou")
    else:
        print("Você utilizou todas as suas seis chances")
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
