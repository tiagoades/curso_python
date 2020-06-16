import re

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu telefone"
email4 = "lalalalala 95437-1254 alalalalalala 1234-1234 lalalala 945674567"

# padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padrao = "[0-9]{4,5}[-]*[0-9]{4}"

# retorno = re.search(padrao, email1)
retorno = re.findall(padrao, email4)

print(retorno)