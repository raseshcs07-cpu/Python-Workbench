# Iterators
# An iterator is an object that contains a countable number of values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, 
# which consist of the methods __iter__() and __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit),"\n")

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

# Q. Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class Mynumbers:
  
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a +=1
    return x 
  
myclass = Mynumbers()
myiter = iter(myclass)

print("\n",next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter),"\n")

# To prevent the iteration from going on forever, we can use the StopIteration statement.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

class Mynumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a<=20:
      x = self.a
      self.a +=1
      return x
    else :
      raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)


# Create a tuple
mytuple = ("apple", "banana", "cherry")
# Create an iterator
myit = iter(mytuple)
# Print the first item
print(next(myit))