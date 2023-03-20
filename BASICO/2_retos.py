"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def retofizzbuzz():
    for n in range(100):
        valor = n+1
        if valor%3 ==0 and valor%5==0:
            print("fizzbuzz")
        elif valor%3==0:
            print("fizz")
        elif valor%5==0:
            print("buzz")
        else:
            print(valor)

retofizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(palabra_1, palabra_2):
    palabra_2=palabra_2[::-1]
    palabra_2=palabra_2.lower().capitalize()
    print(palabra_1,palabra_2)
    if palabra_1 == palabra_2:
        print("La palabra es un anagrama")

anagrama("Amor","Roma")

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    print(sorted(word_one.lower()))
    print(sorted(word_two.lower()))
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Amor"))



"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    fzero=0
    fone= 1 
    for n in range(48):
        print(fzero)
        f_x=  fzero+fone 
        fzero =fone
        fone=f_x

        

fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def esprimo():
    for numero in range(1,101):
        is_divisible = False
        if numero >= 2:
            for dividento in range(2,numero):
                if numero%dividento == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(numero)


esprimo()

def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()



"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse_string(cadena_una):
    cadena_dos=cadena_una[::-1]
    print(cadena_una,cadena_dos)

reverse_string("Hola mundo")


def reverse_string_na(cadena_una):
    tamanio = len(cadena_una)
    cadena=""
    for index in range(0 , tamanio):
        cadena += cadena_una[tamanio-1 - index]

    print(cadena_una,cadena)

reverse_string_na("Hola mundo")