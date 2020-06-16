class ExtratorArgumentosUrl:
	def __init__(self, url):
		if self.urlEhValida(url):
			self.url = url.lower()
		else:
			raise LookupError("Url Invalida!!!")

	def __len__(self):
		return len(self.url)

	def __str__(self):
		moedaOrigem, moedaDestino, valor = self.extrairArgumentos()
		# representacaoString = "Valor: " + valor + " Moeda Origem: " + moedaOrigem + " Moeda Destino" + moedaDestino
		representacaoString = "Valor: {} \nMoeda Origem: {} \nMoeda Destino {}".format(valor, moedaOrigem.capitalize(), moedaDestino.capitalize())
		return representacaoString

	def __eq__(self, outraInstacia):
		return self.url == outraInstacia.url

	@staticmethod
	def urlEhValida(url):
		if url and url.startswith("https://www.bytebank.com.br"):
			return True
		else:
			return False

	def extrairArgumentos(self):

		print(f"URL{self.url}")

		# buscaMoedaOrigem = "moedaorigem"
		# buscaMoedaDestino = "moedadestino"

		buscaMoedaOrigem = "moedaorigem=".lower()
		buscaMoedaDestino = "moedadestino=".lower()
		valor = self.extrairValor()

		# indiceInicialMoedaOrigem = self.url.find("=") + 1
		# indiceFinalMoedaOrigem = self.url.find("&")
		# indiceInicialMoedaDestino = self.url.find("=",(indiceFinalMoedaOrigem +1)) + 1
		# indiceFinalMoedaDestino = self.url.find("&", (indiceFinalMoedaOrigem +1))
		#
		# moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
		# moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

		indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
		indiceFinalMoedaOrigem = self.url.find("&")
		moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

		if moedaOrigem == "moedadestino":
			moedaOrigem = self.verificaMoedaOrigem(buscaMoedaOrigem)

		indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
		indiceFinalMoedaDestino = self.url.find("&valor", indiceInicialMoedaDestino)
		moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

		return moedaOrigem, moedaDestino, valor

	def encontraIndiceInicial(self, moedaBuscada):

		# return self.url.find(moedaBuscada) + len(moedaBuscada) + 1
		return self.url.find(moedaBuscada) + len(moedaBuscada)

	def verificaMoedaOrigem(self, buscaMoedaOrigem):
		print("Alterando o valor da moeda!!!")
		self.url = self.url.replace("moedadestino", "real", 1)
		indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
		indiceFinalMoedaOrigem = self.url.find("&")
		print(self.url)
		return self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

	def extrairValor(self):
		buscaValor = "valor="
		indiceInicialValor = self.encontraIndiceInicial(buscaValor)
		valor = self.url[indiceInicialValor:]
		return valor