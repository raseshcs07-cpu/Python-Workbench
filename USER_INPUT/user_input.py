# userinput
print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")

# Multiple Inputs
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal? ")
fav2 = input("What is your favorite color? ")
fav3 = input("What is your favorite number? ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

import math
x = input("Enter a number:")
y = math.sqrt(float(x))                                 #find the square root of the number:
print(f"The square root of {x} is {y}")

import math
x = input("Enter a number:")
print(f"The square root of {x} is {math.sqrt(float(x))}")

y = True
while y == True:
    x = input("Enter the number:")
    try:
        x= float(x)
        y =False
    except:
        print("wrong input ,try again!")
print("Thank You!")