#Function means chunk of the code that can be called by name to perform a specific task. It can take inputs, process them, and return an output. Functions are reusable blocks of code that help to organize and modularize a program.
def add(x,y):
    z = x + y
    return z 

x = float(input("Enter the value: "))
y = float(input("Enter the value: "))
a = add(x,y)
print("The addition is", a)

