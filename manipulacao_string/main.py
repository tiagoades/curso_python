from ExtratorArgumentosUrl import ExtratorArgumentosUrl

meunome = "Tiago"

# ......01234

# substring = meunome[1]

substring = meunome[1:]

print(substring)

# argumento = "moedaorigem=real"
'''
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valva=1500"

# ......012345678910111213141516

substring1 = argumento[5:11]
print(substring1)

'''

argumento = 'https://www.bytebank.com.br/cambio?moedaorigem=real'

index = argumento.find("=")

print(index)

lista = argumento.split("=")

substring2 = argumento[index + 1:]

print(substring2)
print(lista)

string = 0

print(string is None)

if(string):
	print("Tem algo aqui!!!")
else:
	print("Vazio!!!")

# url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url1 = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=700"
url2 = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1700"
# url = ""

# argumento2 = ExtratorArgumentosUrl(url)
#
# print(argumento2)



argumentoUrl1 = ExtratorArgumentosUrl(url1)
argumentoUrl2 = ExtratorArgumentosUrl(url2)

print(ExtratorArgumentosUrl.urlEhValida(url1))

moedaOrigem, moedaDestino, buscaValor = argumentoUrl1.extrairArgumentos()

moedaOrigem, moedaDestino, buscaValor = argumentoUrl2.extrairArgumentos()

print(moedaOrigem, moedaDestino, buscaValor)

'''

index = url.find("moedaorigem") + len("moedaorigem") + 1

substring3 = url[index:]

print(substring3)

string = "bytebankbytebyte"
stringNova = string.replace("byte","tiago",1)

print(stringNova)

banco1 = "bytebank"
banco2 = "Bytebank".lower()

print(banco1 == banco2)

'''

urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste"

# print(url3.find(urlByteBank))
print(url2.startswith(urlByteBank))


filme = "Vingadores - Era de Ulton"
filme = "Os quase Vingadores - End Game"
filme = "Detonadores  - Os Vingadores"
filmeEhVingadores = filme.startswith("Vingadores")
if filmeEhVingadores:
    print("Esse filme é dos vingadores")
else:
    print("Esse filme não é dos vingadores")

print(len(argumentoUrl1))

print(argumentoUrl1)

print(id(argumentoUrl1))
print(id(argumentoUrl2))

print(argumentoUrl1 == argumentoUrl2)