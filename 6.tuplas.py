#tuplas no se pueden modificar una vez inicializado

mi_tupla = tuple ()
mi_tupla_variante= (32,21)
mi_tupla = (23,1.80,"Raul","Calderon")

print(type(mi_tupla))
print(mi_tupla)

print(mi_tupla[0])
print(mi_tupla[-1])

#print(mi_tupla[-5]) error index


print(mi_tupla.count(23))

print(mi_tupla.index("Raul"))

my_subtuple = mi_tupla+mi_tupla_variante
print(my_subtuple)

print(my_subtuple[2:3])

mi_tupla = list(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

mi_tupla.append("Fin")
mi_tupla.insert(0,10)
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

#del mi_tupla
#print(mi_tupla) borrar algo que no se deberia borrar :)