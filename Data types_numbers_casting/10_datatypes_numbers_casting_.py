# Variables can store data of different types, and different types can do different things.
# Built-in Data Types

'''
x = "Hello World"	                                          str	
x = 20.5	                                                  float	
x = 1j	                                                      complex	
x = ["apple", "banana", "cherry"]	                          list	
x = 20	                                                      int	
x = ("apple", "banana", "cherry")	                          tuple	
x = range(6)	                                              range	
x = {"name" : "John", "age" : 36}	                          dict	
x = {"apple", "banana", "cherry"}	                          set	
x = frozenset({"apple", "banana", "cherry"})                  frozenset	
x = True	                                                  bool	
x = b"Hello"	                                              bytes	
x = bytearray(5)	                                          bytearray	
x = memoryview(bytes(5))                                      memoryview	
x = None	                                                  NoneType

'''


#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print("\n\n",x)
print(y)
print(z,"\n")

print(type(x))
print(type(y))
print(type(z))



import random 
print("\n\n",random.randrange(1,100),"\n\n")


x = str("s1")
y = str(2)
a = float(2)
z = int(3.0)
print(x)
print(y)
print(z)
print(a)


