number1 = 8
print(number1)
number2 = 2.0
print(number2)
name = 'ala' 
print(name)
Number_1_bigger_than_number_2 = number1>number2
print(Number_1_bigger_than_number_2)
# two set variables
if number1 > number2:
    print(" Ten numer jest większy")
else:
    print("Ten numer jest mniejszy")
''' function if, comparing the value of two variables'''
week=7
goal='nauczenie się pythona'

description='Mam na imię {} od {} tygodni uczę się programowania. Moim celem jest {}.' .format(name,week,goal)
print(description)
description2= f'Mam na imię {name} od {week} tygodni uczę się programowania. Moim celem jest {goal}.'
print(description2)