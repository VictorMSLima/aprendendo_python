import random

# print("++++++++++++++++++++++++++++++++",chute , sep="X", end = "!")

# numero1 = 10
# numero2 = "20"
# produto = numero1 * numero2
# print(produto)
#20202020202020202020
def jogar_adivinhacao():

    print("++++++++++++++++++++++++++++++++")
    print("Bem vindo ao jogo de adivinhação")
    print("++++++++++++++++++++++++++++++++")

    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina o seu nível:  "))
    if (nivel == 1):
        total_de_tentativas = 20
    if (nivel == 2):
        total_de_tentativas = 10
    if (nivel == 3):
        total_de_tentativas = 5



    for rodada in range (1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100  "))
        print("Voce digitou: ",chute)

        if (chute < 1 or chute>100):
            print("Você deve digitar um número entre 1 e 100")
            rodada = rodada
            continue

        if (numero_secreto == chute):
            print("Você acertou e fez {} pontos!".format(pontos))
            break

        elif (numero_secreto > chute):
            print("Você errou!O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        else:
            print("Você errou!O seu chute foi maior que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do Jogo")
            

    #print("R$ {:07.2f}".format(4.5))
    #'R$ 0004.50'
    #print("R$ {:07d}".format(46))
    #'R$ 0000046'
if (__name__ == "__main__"):
    jogar_adivinhacao()