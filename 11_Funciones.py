def fun (a,b):
   return a-b
aa=5
b=2
print(fun(aa,b))



def multiplica (a,b):
   print("Funcion de multiplicar")
   print(a*b)
multiplica(5,3)

def multiplica1 (a,b):
   return a*b

valor=multiplica1(5,2)
print(valor)


def print_nombre(nombre,apellido):
   print("Su nombre es {} y su apellido es {}".format(nombre,apellido))


print_nombre(nombre="Raul",apellido="Calderon")


def print_nombre1(nombre,apellido,alias="Sin alias"):
   print("Su nombre es {} y su apellido es {} y su alias es {}".format(nombre,apellido,alias))


print_nombre1("Raul","Calderon") #sin valor 3 dato
print_nombre1("Raul","Calderon","Rulas") #normal

def print_texto (*text):
   for n in text:
      print(n.upper())

print_texto("hola","prueba","dos")