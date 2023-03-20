#clases
"""
class Persona:
    def nombre(name):
        return name
    
persona1 = Persona

print(type(Persona))
print(persona1.nombre("Raul"))"""

class PersonaVacia:
    pass

class Persona:
    def __init__(self,name,surname,alias="Sin alias"): #constructor para establer valores asociados
        self.full_name= f"{name} {surname} {alias}"
        self.__name = name
    def walk(self):
        print(f"{self.full_name} Esta caminando")
    def getnombre(self):
        return self.__name

persona1 = Persona("Raul","Calderon")
print(persona1.full_name)

persona1.walk()
print(persona1.getnombre())
persona2 = Persona("Raul","Calderon","Rulas")

persona2.full_name= "Raul G god"
print(persona2.full_name)
persona2.walk()