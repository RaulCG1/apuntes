#Diccionarios
mi_dicti = dict()
my_dics = {}
#print (type(mi_dicti))
#print (type(my_dics))

my_dics = {"Nombre":"Raul",
           "Apellido":"Raul",
           "Edad":23,
           "Lenguajes":{"VALOR","Swift","C"},
           1:1.80
           }

print(type(my_dics))
print(my_dics)
print(my_dics["Nombre"])
print(my_dics.get("Lenguajes"))
my_dics["Calle"] = "Centeolt"
print(my_dics)

del my_dics["Apellido"]
print(my_dics)


print("Nombre" in my_dics) #comprobacion si existe elemento
print("Rausl" in my_dics)

print(my_dics.items())
print(my_dics.keys())
print(my_dics.values())

my_new_key = dict.fromkeys({"Nombre",1})
print(my_new_key) #crear un dioccionario vacio

my_new_key["Nombre"]= "A"

my_new_key = dict.fromkeys(my_dics)
print(my_new_key) #crear un dioccionario vacio

my_new_key["Nombre"]= "A"


my_new_key = dict.fromkeys(my_dics, ("Raul","Calderon"))
print(my_new_key) #crear un dioccionario vacio

