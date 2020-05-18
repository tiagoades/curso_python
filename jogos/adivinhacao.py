import random

def jogar():
    print("**********************************")
    print("Bem vindos ao jogo de Adivinhação!")
    print("**********************************")

    # numero_secreto = 42

    # podemos ainda utilizar a função int() como alternativa int(random() * 101)
    # função random() do modulo do random importado gera um numero randomico do tipo float entre 0.0 e 1.0 (para gerar de 0 a 100 multiplicamos por 100) o resultado e devolvido com casas decimais ex. 1.01234
    # função round() arredonda o resultado da função random() para cima devolvendo o resultado sem as casa decimais
    # numero_secreto = round(random.random() * 100)

    # função randrange() do modulo random importado gera um numero randomico conforme o range passado para a função (para gerar de 1 a 100 precisamos passar no segundo parametro o valor desejado + 1) esta função devolve um numero inteiro
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")
    nivel = input("Defina o nivel: ")

    while (nivel == "" or not nivel.isdigit() or int(nivel) < 1 or int(nivel) > 3):
        nivel = input("Defina um nivel valido: ")
        # if (nivel != "" and nivel.isdigit()):
        #     nivel = int(nivel)
            # if(nivel <= 1 or nivel >= 3):
            #     nivel = input("Defina um nivel valido: ")

    nivel = int(nivel)

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5

    # print(numero_secreto)

    # rodada = 1

    # while (rodada <= total_de_tentativas):
    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")

        print("Você digitou: ", chute_str)

        chute = int(chute_str)

        if( chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("você errou! O seu chute foi maior que o numero secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("você errou! O seu chute foi menor que o numero secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))


            pontos_perdidos = abs(numero_secreto - chute)
            pontos = round((pontos - pontos_perdidos) / 3)

        # rodada = rodada + 1
    print("Fim do jogo!!!")

if(__name__ == "__main__"):
    jogar()