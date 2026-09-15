# Comparison Operators
x = 5
y = 3
      
print(x == y)                                        #equal
print(x != y)                                        #not equal
print(x > y)                                         #Greater than
print(x < y)                                         #Less than
print(x >= y)                                        #Greater than or equal to 
print(x <= y)                                        #Less than or equal to 

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#  Logical Operators
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10


# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)                       # returns True because z is the same object as x
print(x is y)                       # returns False because x is not the same object as y, even if they have the same content
print(x == y)                       # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)                      # returns False because z is the same object as x
print(x is not y)                      # returns True because x is not the same object as y, even if they have the same content
print(x != y)                          # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Membership Operators
x = ["apple", "banana"]
print("banana" in x)                    # returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)             # returns True because a sequence with the value "pineapple" is not in the list

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operators
print(6 & 3)                            #Sets each bit to 1 if both bits are 1           [and]
print(6|3)                              #Sets each bit to 1 if one of two bits is 1.     [or]
print(6^3)                              #Sets each bit to 1 if only one of two bits is 1 [xor]
print(~3)                               #Inverts all the bits                             not]
print(3 << 2)                           #  Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3>>2)                             #  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


"""
Precedence Order
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	               Description	Try it

()	                       Parentheses	
**	                       Exponentiation	
+x  -x  ~x	               Unary plus, unary minus, and bitwise NOT	  ~x = -(x + 1)
*  /  //  %	               Multiplication, division, floor division, and modulus	
+  -	                   Addition and subtraction	
<<  >>	                   Bitwise left and right shifts	
&	                       Bitwise AND	
^	                       Bitwise XOR	
|	                       Bitwise OR	
==  !=  >  >=  <  <= 	   Comparisons, identity, and membership operators	
 is  is not  in  not in 
not	                       Logical NOT	
and	                       AND	
or	                       OR
"""

# Create variables
a = 15
b = 4
# Print modulus
print(a % b)
# Print floor division
print(a // b)
# Print power
print(a ** b)
# Add 10 to a
a += 10

# 8 << 2 = 8 × 2²
    #    = 8 × 4
    #    = 32
print(1 or 2 and 3)