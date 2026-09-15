a = "Hello"
b = "World"
c = a + b
print(c)

# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)
# can be  in python variable 

# f-string - f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations
age=19
txt= f"My name is Rasesh , I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


# Escape Character.   \
txt = "We are the so - called \"Vikings\" from the north."
print(txt)

# \'	Single Quote
txt = 'It\'s alright.'
print(txt) 
	
# \\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt) 
	
# \n	New Line	
txt = "Hello\nWorld!"
print(txt) 

# \r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

# \t	Tab	
txt = "Hello\tWorld!"
print(txt) 

# \b	Backspace	
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

# \ooo	Octal value	

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

# Define octal values
octal_num = 0o12  
print(octal_num)  # Output: 10 (Python automatically prints it as a decimal)
# Convert decimal to octal string
decimal_val = 10
octal_str = oct(decimal_val)
print(octal_str)  # Output: '0o12'
# decimal- a>97 , b>98 ....... z>122 
# octal a>97\8=12+1 , 12\8=1+4 , 1\8=0+1 ===141
# z>122\8=15+2 , 15\8=1+7 , 1\8=0+1 ===172

# \f	Form Feed	

# \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
# Decimal:       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# Hexadecimal:   0 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F
# 101\16 = 6+5 ===65
# 108\16 = 6+12 ===6C

"""
Method	Description
capitalize()	 Converts the first character to upper case
casefold()	     Converts string into lower case
center()	     Returns a centered string
count()	         Returns the number of times a specified value occurs in a string
encode()	     Returns an encoded version of the string
endswith()	     Returns true if the string ends with the specified value
expandtabs()	 Sets the tab size of the string
find()	         Searches the string for a specified value and returns the position of where it was found
format()	     Formats specified values in a string
format_map()	 Formats specified values in a string
index()	         Searches the string for a specified value and returns the position of where it was found
isalpha()      	 Returns True if all characters in the string are in the alphabet
isalnum()	     Returns True if all characters in the string are alphanumeric
isdecimal() 	 Returns True if all characters in the string are decimals
isascii()	     Returns True if all characters in the string are ascii characters
isdigit()      	 Returns True if all characters in the string are digits
isidentifier()   Returns True if the string is an identifier
isnumeric()      Returns True if all characters in the string are numeric
islower()	     Returns True if all characters in the string are lower case
isprintable()	 Returns True if all characters in the string are printable
istitle()      	 Returns True if the string follows the rules of a title
isspace()	     Returns True if all characters in the string are whitespaces
isupper()      	 Returns True if all characters in the string are upper case
join()	         Joins the elements of an iterable to the end of the string
ljust()	         Returns a left justified version of the string
lower()          Converts a string into lower case
maketrans()      Returns a translation table to be used in translations
lstrip()	     Returns a left trim version of the string
partition()      Returns a tuple where the string is parted into three parts
replace()	     Returns a string where a specified value is replaced with a specified value
rfind()	         Searches the string for a specified value and returns the last position of where it was found
rindex()	     Searches the string for a specified value and returns the last position of where it was found
rjust()	         Returns a right justified version of the string
rpartition()	 Returns a tuple where the string is parted into three parts
rsplit()	     Splits the string at the specified separator, and returns a list
rstrip()	     Returns a right trim version of the string
split()	         Splits the string at the specified separator, and returns a list
splitlines()	 Splits the string at line breaks and returns a list
startswith()	 Returns true if the string starts with the specified value
strip()	         Returns a trimmed version of the string
swapcase()	     Swaps cases, lower case becomes upper case and vice versa
title()	         Converts the first character of each word to upper case
translate()	     Returns a translated string
upper()	         Converts a string into upper case
zfill()	         Fills the string with a specified number of 0 values at the beginning
"""

a = "My name is Rreveal , \tMy name is rasesh"
print("\n\n\n",a.zfill(25))
print(a.upper())

# table = str.maketrans("r","R")                         # translation table
table = str.maketrans("R", "A") 
print(a.translate(table))  
print(a.title())
print(a.swapcase())
print(a.strip())                                         #\n
print(a.startswith("is"))
print(a.splitlines())
print(a.split())
print(a.rsplit())
print(a.split(" ", 1))
print(a.rpartition(" "))
print(a.rjust(44))
print(a.rindex("name"))
print(a.rfind("name"))
print(a.replace("Rreveal" , "rReveal"))
print(a.partition("name"))
print(a.lstrip())	
# table = str.maketrans("R", "A") 
print(a.lower())
print(a.ljust(10))
# print(a.join()).       a = " "
# print(a.join(["My", "name", "is", "Rasesh"]))
print(a.isupper())
print(a.isspace())
print(a.islower())
print(a.isprintable())
print(a.isnumeric())
print(a.istitle())
print("name".isidentifier())
print(a.isdigit())
print(a.isascii())
print(a.isalpha())
print(a.isalnum())
print(a.isdecimal())
print(a.index("name"))
print(a.format())
print(a.format_map(a))
print(a.find("name"))
print(a.expandtabs(10))
print(a.endswith("rasesh"))
print(a.encode())
print(a.count("name"))
print(a.center(11))
print(a.casefold())
print(a.capitalize())

a = "\n\nMy name is {} and I am {} years old"
print(a.format("Rasesh", 20))

a = "My name is {name}"
data = {"name": "Rasesh"}
print(a.format_map(data))


# Create the variable
txt="Hello,World!"

# Print characters from index 2 to 5
print("\n\n",txt[2:5])
# Print in upper case
print(txt.upper())
# Create the name variable
name="Python"
# Print using an f-string
print(f"I love  {name}")



