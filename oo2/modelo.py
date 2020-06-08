class Programa:

#cls - convenção usado nas classes mãe (superclasses)
#self - convenção usado nas classes filhas (subclasses)
#self == cls

	pre = "Babozeira"

	@classmethod
	def xpto(cls):
		print(f'{cls.pre}')

	@staticmethod
	def asdf():
		def log():
			return f'Isso é um log qualquer'

	def __init__(self, nome, ano):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0

	@property
	def likes(self):
		return self._likes

	def dar_likes(self):
		self._likes += 1

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome.title()

	# def imprime(self):
	# 	print(f'{self._nome} - {self.ano} - {self._likes} Likes')

	def __str__(self):
		return f'{self.nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
	def __init__(self, nome, ano, duracao):
		super().__init__(nome, ano)
		self.duracao = duracao

		__class__.xpto()

	def __str__(self):
		return  f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
	def __init__(self, nome, ano, temporadas):
		super().__init__(nome, ano)
		self.temporadas = temporadas

	def __str__(self):
		return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
	def __init__(self, nome, programas):
		self.nome = nome
		self._programas = programas

	@property
	def listagem(self):
		return self._programas

	def __len__(self):
		return len(self._programas)

	def __getitem__(self, item):
		return self._programas[item]

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

demolidor.dar_likes()
demolidor.dar_likes()

# print('{} - {} - {} : {}'.format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
# print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} : {atlanta.likes}')


filmes_e_serie = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_serie)

# playlist = {"findesemana": Playlist("fimdesemana", filmes_e_serie)}

# print(f'O tamanho do playlist é: {len(playlist_fim_de_semana)}')

# print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

print(vingadores in playlist_fim_de_semana)

print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana:

	# if (hasattr(programa, "duracao")):
	# 	detalhes = programa.duracao
	#
	# else:
	# 	detalhes = programa.temporadas

	# print(f'{programa.nome} - {detalhes} D - {programa.likes}')

	# programa.imprime()

	print(programa)