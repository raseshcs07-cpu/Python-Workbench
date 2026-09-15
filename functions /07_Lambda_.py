# A lambda function is a small anonymous [ without a name ] function.

# ex.1  
# Add 10 to argument a, and return the result

x = lambda a :  a + 10 
print(x(5), end= '\n\n')
print()

# ex. 2
# Multiply argument a with argument b and return the result:

x= lambda a , b : a*b
print(x(5,6), end= '\n\n')


# ex.3
# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2),end='\n\n')


# Lambda Functions
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# ex.4 
def function(n):
    return lambda  a : a*n
doubled = function(2)
print(doubled(11),end='\n\n')


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11),end='\n\n')



# use the same function definition to make both functions, in the same program:
# ex.5

def multipication(n):
   return lambda a : a*n

doubled = multipication(2)
mytripler = multipication(3)
mymultiplier = multipication(3454325432432)

print(doubled(11),end='\n\n')
print(mytripler(11),end='\n\n')
print(mymultiplier(11),end='\n\n\n')





# lambda with built-in function.
# like : map() ,  filter() , sorted().


# map()
# The map() function applies a function to every item in an iterable:

# Double all numbers in a list:
# ex. 6

numbers = [1,2,3,4,5]
doubled = list(map(lambda x : x*2 , numbers))
print(doubled,end='\n\n\n\n')

# squares
# ex. 7

numbers = [1,2,3,4,5]
squared = list(map(lambda x : x**2 , numbers))
print(doubled,end='\n\n\n\n')

# ex.8

list1 = [1, 2, 3]
list2 = [10, 20, 30]

summed = map(lambda x, y: x + y, list1, list2)                    # Add elements of two lists positionally

print(list(summed),end='\n\n\n\n')


# ex. 9

scores = [45, 82, 59, 91]

results = map(lambda score: "Pass" 
              if score >= 60 
              else "Fail",
                scores)           # Tag numbers as Pass or Fail

print(list(results),end='\n\n\n\n')
# Output: ['Fail', 'Pass', 'Fail', 'Pass']




# filter()
# he filter() function creates a list of items for which a function returns True:

# ex. 10
# Filter out odd numbers from a list:

numbers = [1,2,3,4,556,77,8,90]
odd_numbers = list(filter(lambda x : x%2 != 0, numbers))
print(odd_numbers,end='\n\n\n\n')


#  sorted()
# function can use a lambda as a key for custom sorting:

# ex. 11
# Sort a list of tuples by the second element:

students = [ ("Rasesh",19) , ("Tanishk",22), ("Harish",46)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students,end='\n\n\n\n')

# ex. 12
# Sort strings by length:

words = [ "apple", "cherry", "banana" , "pie"]
sorted_words = sorted(words , key= lambda x: len(x))
print(sorted_words,end='\n\n\n\n')
