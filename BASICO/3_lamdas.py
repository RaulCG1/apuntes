#lambdas funciones anonimas


suma =lambda a,b: a+b

print(suma(10,20))

mult =lambda a,b: a*b-3
print(mult(10,20))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))
