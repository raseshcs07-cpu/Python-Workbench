# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

# coution:
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never 
# terminates, or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# ex. 1
def factorial(n):
    if(n==0 or n==1):                                       # Base case  
        return 1 
    else:                                                   # recursive case
        return n*factorial(n-1)
print(factorial(5),end="\n\n\n")

# recursion
'''
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5*4*3*2*1

'''

# ex. 2

def countdown(n):
    if(n<=0):
        print("\ndone!\n")
    else:
        print(n)
        countdown(n-1)
countdown(8)
print()


# Base Case and Recursive Case
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.


# ex. 3
#Fibonacci sequence: 

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7),end="\n\n")
 

# Recursion with Lists:

# ex. 4
def sum_list(num):
   if len(num) == 0:                                        # length (the number of items)
    return 0
   else:
    return num[0] + sum_list(num[1:])

my_list = [1,2,3,4,56,67,8]
print(sum_list(my_list),end="\n\n")
   

'''
Call 1: sum_list([1, 2, 3, 4, 5])
List length is 5 (Not 0) $\rightarrow$ 
Returns 1 + sum_list([2, 3, 4, 5])

Call 2: sum_list([2, 3, 4, 5]
)List length is 4 (Not 0) $\rightarrow$ 
Returns 2 + sum_list([3, 4, 5])

Call 3: sum_list([3, 4, 5])
List length is 3 (Not 0) $\rightarrow$
 Returns 3 + sum_list([4, 5])

Call 4: sum_list([4, 5])
List length is 2 (Not 0) $\rightarrow$
 Returns 4 + sum_list([5])

Call 5: sum_list([5])
List length is 1 (Not 0) $\rightarrow$ 
Returns 5 + sum_list([])

Call 6: sum_list([])
List length is 0 $\rightarrow$ 
Hits Base Case! Returns 0.




Call 6 returns  0 
Call 5 resolves 5 + 0 = 5
Call 4 resolves 4 + 5 = 9
Call 3 resolves 3 + 9 = 12
Call 2 resolves 2 + 12 = 14
Call 1 resolves 1 + 14 = 15

'''


# ex. 5
# Find the maximum value in a list:

def find_max(num):
   if len(num)==1:                       # Base case: if the list has only 1 item, that's the max.
      return num[0]                      # Recursive step: get the max of the rest of the list.
   else:  
      max_of_rest = find_max(num[1:])

      # Corrected comparison: return the larger of the two
      return num[0]                    if num[0] > max_of_rest      else max_of_rest


my_list = [3, 7, 2, 9, 1]
print(find_max(my_list),end="\n\n\n")



# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

# ex. 6

import sys
print(sys.getrecursionlimit(),end="\n\n\n")

# ex. 7
# increase the limit

import sys
sys.setrecursionlimit(500000)
print(sys.getrecursionlimit(),end="\n\n\n")
