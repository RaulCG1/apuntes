#Expresiones regulares en python
import re

my_string= "Esta es la leccion numero 7: Leccion llamada expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

match = re.match("Esta es la leccion",my_string,re.I) #match busca desde el principio

span=match.span()
print(match.span())
starts,ends= span

print(my_string[starts:ends])

match = re.match("Esta no es la leccion",my_other_string)
#if match != None
if not (match == None):
    span=match.span()
    print(match)
    print(match.span())
    starts,ends= span
    print(my_other_string[starts:ends])



#print(re.match("Expresiones Regulares",my_string))


#SEARCH

seacr=re.search("leccion", my_string,re.I)
print(seacr)
span=seacr.span()
print(seacr.span())
starts,ends= span

print(my_string[starts:ends])

#findall

buscartodo=re.findall("leccion",my_string,re.I)
print(buscartodo)

#split

split= re.split("cc",my_string,re.I)

print(split)

#sub

subs = re.sub("Regulares","regulares",my_string,re.I)
print(subs)
subs = re.sub("[l|L]eccion","LECCION",my_string)
print(subs)


#expresiones regualres personalizadas o patron

#patterns

pattern = r'[lL]eccion'

print(re.findall(pattern,my_string))

pattern = r'[lL]eccion|expresiones'
print(re.findall(pattern,my_string))


pattern = r'[a-z]'
print(re.findall(pattern,my_string))

pattern = r'[0-9]'
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r'[A-Z]'
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r'\d'
print(re.findall(pattern,my_string))

pattern = r'\D'
print(re.findall(pattern,my_string))


pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "calderon.garsia.raul@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "calderon.garsia.raul@gmail.com"
print(re.findall(pattern, email))