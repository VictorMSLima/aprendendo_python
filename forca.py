

def jogar_forca():

    print("++++++++++++++++++++++++++++++++")
    print("+++Bem vindo ao jogo da Forca+++")
    print("++++++++++++++++++++++++++++++++")

    palavra_secreta = "bananas".lower()

    enforcou = False
    acertou = False
    erros = 0
    

    chutes = []
    while (not enforcou and not acertou):

        qtd_letras = 0
        
        print("\nJogando ...")

        chute = input("Digite uma letra:  ")
        chute = chute.strip().lower()
        chutes.append(chute)

        for letra in palavra_secreta:
            if (letra in chutes):   
                print(letra, end=" ")
                qtd_letras += 1
                print("------------------------------",qtd_letras, len(palavra_secreta) )
                if (len(palavra_secreta) <= qtd_letras ):
                    acertou = True
            else:
                print("_", end=" ")

        if not (chute in palavra_secreta):
            erros += 1

        enforcou = erros == 6

if (__name__ == "__main__"):
    jogar_forca()