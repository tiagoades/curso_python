import random

def jogar():
	print("**********************************")
	print("***Bem vindos ao jogo de Forca!***")
	print("**********************************")

	arquivo = open("palavras.txt", "r")
	palavras = []

	for linha in arquivo:
		linha = linha.strip()
		palavras.append(linha)

	arquivo.close()

	numero = random.randrange(0, len(palavras))

	# palavra_secreta = "banana".upper()
	palavra_secreta = palavras[numero].upper()
	# letras_acertadas = ["_","_","_","_","_","_"]
	# letras_acertadas = []
	letras_acertadas = ["_" for letra in palavra_secreta]

	inteiros = [1, 3, 4, 5, 7, 8, 9]
	pares = [x for x in inteiros if x % 2 == 0]
	# for letra in palavra_secreta:
	# 	letras_acertadas.append("_")

	enforcou = False
	acertou = False
	erros = 0

	print(letras_acertadas)

	while(not acertou and not enforcou):

		chute = input("Qual a letra?")
		chute = chute.strip().upper()
		tentativas = 6

		if(chute in palavra_secreta):
			index = 0
			for letra in palavra_secreta:
				if(chute == letra):
					letras_acertadas[index] = letra
				index += 1
			if ("_" not in letras_acertadas):
				acertou = True
				break
		else:
			erros += 1
			print("A letra {} não contem na palavra, você tem mais {} tentativas".format(chute, tentativas - erros))
			if(erros == tentativas):
				enforcou = True
				break

		# enforcou = erros == tentativas
		# acertou = "_" not in letras_acertadas

		print(letras_acertadas)

	if(acertou):
		print("Você Ganhou!")
	else:
		print("Você perdeu!")

	print("Fim do jogo!!!")

if(__name__ == "__main__"):
	jogar()
