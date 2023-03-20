#ciclos

a=0
while a<10:
    print(a)
    a += 2
#elif no valido
else: #no es necesario
    print("La condicion es mayor o igual a 10")

a=0

while a < 20:
    print("Es menor a 20 y su valor es {}".format(str(a)))
    a += 2
    if a == 15:
        print("Es igual a 15")
    elif a == 18:
        print("Es 18 y se detiene")
        break
    else:
        print("NO es ni 15 y ni 18")



mi_lista = [23,21,21,32,22]

for n in mi_lista:
    print(n)

mi_tupla = (23,1.80,"Raul","Calderon")
for n in mi_tupla:
    print(n)
    if n == "Raul":
        print("salimos de aqui")
        break

my_setdos = {1,2,3,"Raul"}
for n in my_setdos:
    print(n)
my_dics = {"Nombre":"Raul",
           "Apellido":"Raul",
           "Edad":23,
           "Lenguajes":{"VALOR","Swift","C"},
           1:1.80
           }

for n in my_dics:
    print(n)
for n in range(10):
    print(n)


