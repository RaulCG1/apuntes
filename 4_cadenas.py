#cadenas


cadenas= "Hola cadena"

cadena_salto= "Hola \naa"
cadena_salto= "Hola \ttabulacion"
cadena_salto= "\\tHola \\ntabulacion"
print(len(cadenas))
print(cadena_salto)

#borrar

nombre,apeido , age= "Raul","Calderon",23
print("Mi nombre es {} {} y mi edad  es {}".format(nombre,apeido,age))
print("Mi nombre es %s %s y mi edad  es %d" %(nombre,apeido,age))

print(f"Mi nombre es {nombre} {apeido} y mi edad  es {age}")

#desampaquetar caractares
lenguaje = "Python"
a,b,c,d,e,f= lenguaje
#print(a)
#print(b)
print(lenguaje.capitalize())

print(lenguaje.upper())
print(lenguaje.count("y"))
print(lenguaje.isnumeric())
print(lenguaje.upper().isupper())
print(lenguaje.replace("y","s"))
print(lenguaje.startswith("A"))
#division

lenguaje_slice = lenguaje[0:6:2]

reversed_lenguaje = lenguaje[:: -1]
#print(lenguaje_slice)


