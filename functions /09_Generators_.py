# Generators are functions that can pause and resume their execution.
# The code inside the function is not executed yet, it is only compiled. 
# The function only executes when you iterate over the generator.

# ex.1

def my_generator():
    yield 1
    yield 2
    yield 3 

for value in my_generator():
 print("\n",value,"\n")


#  The yield Keyword -  makes function a generator .
#  when yield is encountered , the function's state is saved , and value is returned . The next time the generator is called 
# , it continues from where it let off .

# ex.2

def count_up_to(n):
   count=1
   while count <=n:
      yield count
      count+=1

for num in count_up_to(5):
   print(num,"\n")


# Generators Saves Memory
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

# ex. 3
# Generator for large sequences:

def large_sequence(n):
   for i in range(n):
      yield i 

gen = large_sequence(100000)
print(next(gen))
print(next(gen))
print(next(gen),"\n")


# Using next() with Generators - manually iterate through a generator

# ex. 4
def simple_gen():
   yield "Rasesh"
   yield "Tanishk"
   yield "Love"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen),"\n\n")
# print(next(gen))                        StopIteration 


# Generator Expressions
# List comprehension - creates a list

# ex. 5
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator

# ex. 6
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp),"\n\n")


# Calculate sum of squares without creating a list

# ex. 7
total_sum = sum(x ** x   for x in range(11) )          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(total_sum) 

# ex. 8
total = sum(x * x for x in range(10))
print(total,"\n\n")


# Fibonacci Sequence Generator

# ex. 9
# Generate 100 Fibonacci numbers:

def fibonacci_numbers():
   a , b = 0, 1
   while True:
      yield a
      a, b = b, a + b

gen = fibonacci_numbers()                          # Get first 100 Fibonacci numbers
for _ in range(100):
   print(next(gen), "\n")


# Generator Methods

# ex. 10
#  send() - send a value to the generator:

def echo_generator():
   while True :
      recieved = yield
      print("Recieved:",recieved)

gen = echo_generator()
next(gen)                                            # Prime the generator
gen.send("Hello")
gen.send("World\n\n")


#  close() - stops the generator:
# ex. 11

def my_gen():
   try:
      yield 1
      yield 2
      yield 3
   finally:
      print("Generator closed\n\n")

gen = my_gen()
print(next(gen),"\n")
gen.close()




#  QuES. 1

# Create the greet function
def greet(name):
 print("Hello" +  name)

# Call greet
greet("Emil")
