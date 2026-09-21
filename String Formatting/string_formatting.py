# String Formatting
# F-Strings
txt = f"The price is 49 dollars"
print(txt)

# Placeholders & modifiers
price = 59
txt = f"The  price is {price} dollars!"
print ( txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59 
txt = f"The price is {price:2f} dollars"
print(txt)

txt = f"The price is {95:.2f} dollars"
print(txt)

# Operations in F-Strings
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconvertor(x):
    return x*0.3048
txt=f"The plane is flying at a {myconvertor(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

"""
Formatting       Types
:<		    Left aligns the result (within the available space)
:>		    Right aligns the result (within the available space)
:^		    Center aligns the result (within the available space)
:=		    Places the sign to the left most position
:+		    Use a plus sign to indicate if the result is positive or negative
:-		    Use a minus sign for negative values only
: 		    Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		    Use a comma as a thousand separator
:_		    Use a underscore as a thousand separator
:b		    Binary format
:c		    Converts the value into the corresponding Unicode character
:d		    Decimal format
:e		    Scientific format, with a lower case e
:E		    Scientific format, with an upper case E
:f		    Fix point number format
:F		    Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		    General format
:G		    General format (using a upper case E for scientific notations)
:o		    Octal format
:x		    Hex format, lower case
:X		    Hex format, upper case
:n		    Number format
:%		    Percentage format
"""

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')
txt = f"The price is {x:F} dollars."
print(txt)
#same example, but with a lower case f:
txt = f"The price is {x:f} dollars."
print(txt)

#Use "%" to convert the number into a percentage format:
txt = f"You scored {0.25:%}"
print(txt)
#Or, without any decimals:
txt = f"You scored {0.25:.0%}"
print(txt)

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# Create a variable
price = 49
# Create an f-string
txt = f"The price is {price} dollars"
# Print the result
print(txt)