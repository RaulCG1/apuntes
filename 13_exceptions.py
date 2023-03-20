# manejo de errores

try:
    print("hoLa"+str(5))
except:
    print("No se puede sumar string y numeros")
else: #se ejecuta cuando se mete al ciclo try
    print("si le sabe")
finally: #se ejecuta siempre
    print("Acabo")



numero_uno= 5
numero_dos= 6

numero_dos= "Numero dos"

try:
    print(numero_uno+numero_dos)
except:
    print("NO se puede sumar numero y str")

#exepciones por  tipo

try:
    print(numero_uno+numero_dos)
except TypeError: #solo captura errores de ese tipo 
    print("Se ha producido un error de TypeError")
except ValueError: #solo captura errores de ese tipo 
    print("Se ha producido un error de ValueError")


#captura la informacion del errror
try:
    print(numero_uno+numero_dos)
except Exception as error: #solo captura errores de ese tipo 
    print("Se ha producido un error de TypeError")
    print(error)
