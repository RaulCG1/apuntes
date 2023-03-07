#sets
my_sets = set({21,24,25})
my_setdos = {}
print(type(my_sets))
my_setdos = {1,2,3,"Raul"}
print(type(my_setdos))

print(len(my_setdos))
my_setdos.add("A")
print(my_setdos)

print(my_setdos) #no es estructura ordenada y no admite repetidos

my_setdos.remove("Raul")
print("Raul" in my_setdos) #comprobacion si existe elemento
print("Rausl" in my_setdos)

my_setdos.clear()
my_setdos.update(my_sets)
print(my_setdos)

my_lista = list(my_sets)

print(type(my_lista))
print(my_lista) #evitar hacer esto riesgo a no conocer la ubicacion del elemento 1 

del my_setdos
my_setdos= {"Python","C","Java"}

my_new_set= my_setdos.union(my_sets)
print(my_new_set)


print(my_new_set.difference(my_setdos))

print(my_new_set.intersection(my_setdos))