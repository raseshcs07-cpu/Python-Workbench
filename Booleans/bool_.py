
print(10 > 9)
print(10 == 9)
print(10 < 9)

# bool() function 
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
 def __len__(self):
  return 0
myobj =myclass()
print(bool(myobj))

def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x=200
print(isinstance(x,int))

# Print the result of 10 > 9
print(10 > 9)
# Print the result of 10 == 9
print(10 == 9)
# Print the result of bool("Hello")
print(bool("Hello"))
# Print the result of bool(0)
print(bool(0))