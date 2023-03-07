#listas

mi_lista = list()
mi_otra_lista = [ 23, 1.80,"Raul","Calderon"]
print(len(mi_lista))

mi_lista = [23,21,21,32,22]
print(mi_lista)


print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[2])
print(mi_otra_lista[-1])
print(mi_lista.count(21))
#print(mi_otra_lista[-5]) #errores de indice

edad,altura,nombre,apellido = mi_otra_lista


new_lista = mi_lista+mi_otra_lista
print(new_lista)
new_lista.append("Manzana")
new_lista.insert(1,"azl")
new_lista.reverse()

print(new_lista[0:2])