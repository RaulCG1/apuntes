#orden function alto

def suma_ini(a):
    return a+1

def suma_five(a):
    return a+5


def suma(a,b,f):
    return f(a+b)


print(suma(1,2,suma_five))

#Closures 

def sum_ten(a):
    def add(valor):
        return  valor+10+a
    
    return add
    

add_closure=sum_ten(1)

print(add_closure(10))

print(sum_ten(2)(4))    


# map
numeros = [1,5,9,20,21]

def multiplica_dos(numero):
    return numero*2

print(list(map(multiplica_dos,numeros)))
print(list(map(lambda numero: numero*2,numeros)))

#filtros

def filtra_num(numero):
    if numero > 10:
        return True
    else:
        return False
print(list(filter(filtra_num,numeros)))

print(list(filter(lambda number:number>10,numeros)))

from functools import reduce
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numeros))