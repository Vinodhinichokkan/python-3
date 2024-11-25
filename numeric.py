#numeric data types

#integer type

price = 100
best_price= int(80)
print(type(price))
print(isinstance(best_price,int))   #<class 'int'>
                                    #True


# float type

gpa = 3.28
y = float(1.14)
print(type(gpa))   #<class 'float'>


#complex type

comp_value = 5+3j
print(type(comp_value))     #<class 'complex'>
print(comp_value.real)      #5.0
print(comp_value.imag)      #3.0


#Built-in functions for numbers

print(abs(gpa))   #abs--->it gives the same value if its in negative it give output as positive
   #3.28
print(abs(gpa * -1))  #3.28

print(round(gpa))   #3

print(round(gpa, 1))  #3.3

import math
print(math.pi)      #3.141592653589793
print(math.sqrt(64)) #8.0
print(math.ceil(gpa)) #4
print(math.floor(gpa)) #3


