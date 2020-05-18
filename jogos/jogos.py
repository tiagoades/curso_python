import forca
import adivinhacao

def escolher_jogo():
	print("**********************************")
	print("***Bem vindos ao jogo de Forca!***")
	print("**********************************")

	print("Qual o jogo que deseja?")
	print("(1)Forca (2)Adivinhação")
	jogo = input("Escolha o jogo: ")

	while (jogo == "" or not jogo.isdigit() or int(jogo) < 1 or int(jogo) > 2):
	    jogo = input("Escolha um jogo valido: ")

	jogo = int(jogo)

	if (jogo == 1):
		forca.jogar()
	elif (jogo == 2):
		adivinhacao.jogar()

if(__name__ == "__main__"):
	escolher_jogo()