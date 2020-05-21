import random

def jogar():

	imprime_mensagem_abertura()
	palavra_secreta = carrega_palavra_secreta()
	letras_acertadas = inicializa_letra_acertada(palavra_secreta)
	print(letras_acertadas)

	# Exemplo de retona os valores pares e guarda na lista
	# inteiros = [1, 3, 4, 5, 7, 8, 9]
	# pares = [x for x in inteiros if x % 2 == 0]
	# for letra in palavra_secreta:
	# 	letras_acertadas.append("_")

	enforcou = False
	acertou = False
	erros = 0
	tentativas = 7

	while(not acertou and not enforcou):

		chute = pede_chute()

		if(chute in palavra_secreta):
			marca_chute_correto(palavra_secreta, chute, letras_acertadas)
		else:
			erros += 1
			print("A letra {} não contem na palavra, você tem mais {} tentativas".format(chute, tentativas - erros))
			desenha_forca(erros)

		enforcou = erros == tentativas
		acertou = "_" not in letras_acertadas

		print(letras_acertadas)

	if(acertou):
		imprime_mensagem_vencedor()
	else:
		imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
	print("**********************************")
	print("***Bem vindos ao jogo de Forca!***")
	print("**********************************")

def carrega_palavra_secreta():
	arquivo = open("palavras.txt", "r")
	palavras = []

	for linha in arquivo:
		linha = linha.strip()
		palavras.append(linha)

	arquivo.close()

	numero = random.randrange(0, len(palavras))

	# palavra_secreta = "banana".upper()
	palavra_secreta = palavras[numero].upper()
	return palavra_secreta

def inicializa_letra_acertada(palavra):
	return ["_" for letra in palavra]

def pede_chute():
	chute = input("Qual a letra?")
	return chute.strip().upper()

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
	index = 0
	for letra in palavra_secreta:
		if (chute == letra):
			letras_acertadas[index] = letra
		index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
	jogar()
