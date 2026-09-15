# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

# Create the tuple
fruits = ("apple", "banana", "cherry")
# Print the second item
print(fruits[1])
# Print the number of items
print(len(fruits))
# Unpack the tuple
(a, b, c) = fruits
# Print b
print(b)