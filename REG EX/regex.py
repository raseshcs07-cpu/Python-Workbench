# Regular Expression
# RegEx ek pattern hota hai jisse hum text ke andar specific cheez ko find, check, ya replace kar sakte hain.
"""
Important RegEx symbols

Ye sabse important part hai.

Pattern	Meaning	Example
\d	digit	5
\D	not a digit	A
\w	letter/digit/underscore	A, 5, _
\W	not \w	@, #
\s	whitespace	space
\S	not whitespace	A
.	any character	a, 7, @
^	beginning	starts with
$	ending	ends with
"""
# #Check if the string starts with "The" and ends with "Spain":
import re 
txt = "The rain in spain"
x = re.search("^The.*spain$",txt)

if x:
    print("\nYes!We have a match!\n")
else:
    print("No matches!")



"""
Function	Description
findall	     Returns a list containing all matches
search	     Returns a Match object if there is a match anywhere in the string
split	     Returns a list where the string has been split at each match
sub	         Replaces one or many matches with a string
"""

# Metacharacters are characters with a special meaning:
"""
Character	Description	                                                                Example
[]	        A set of characters	                                                        "[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	"\d"	
.	        Any character (except newline character)	                                "he..o"	
^	        Starts with	                                                                "^hello"	
$	        Ends with	                                                                "planet$"	
*	        Zero or more occurrences	                                                 "he.*o"	
+	        One or more occurrences	                                                     "he.+o"	
?	        Zero or one occurrences	                                                     "he.?o"	
{}	        Exactly the specified number of occurrences	                                  "he.{2}o"	
|	        Either or	                                                                "falls|stays"	
()	        Capture and group	 
"""

import re 
txt = "The rain in spain"
x = re.findall("[a-m]",txt)
print(x,"\n")


import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)


import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)


import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)


import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)


import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)


import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# You can add flags to the pattern when using regular expressions.
"""
Flag	        Shorthand	  Description	
re.ASCII	    re.A	      Returns only ASCII matches	
re.DEBUG		              Returns debug information	
re.DOTALL	    re.S	      Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I	      Case-insensitive matching	
re.MULTILINE	re.M	      Returns matches at the start/end of each line	
re.NOFLAG		              Specifies that no flag is set for this pattern	
re.UNICODE	    re.U	      Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	                  re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable
"""

import re
txt = "Åland"
#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))
#Without the flag, the example would return all character:
print(re.findall("\w", txt))
#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))


import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.DEBUG))


import re
txt = """Hi
my
name
is
Sally"""
#Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))
#This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt))
#Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S))


import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE))
#Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I))


import re
txt = """There
aint much
rain in 
Spain"""
#Search for the sequence "ain", at the beginning of a line:
print(re.findall("^ain", txt, re.MULTILINE))
#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^ain", txt))
#Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M))


import re
txt = "Åland"
#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))
#Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))


import re
text = "The rain in Spain falls mainly on the plain"
#Find and return words that contains the phrase "ain":
pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""
print(re.findall(pattern, text, re.VERBOSE))
#The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text))
#Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X))


# Special Sequences
"""
Character	 Description	                                                                                     Example	
\A	         Returns a match if the specified characters are at the beginning of the string	                     "\AThe"	
\b	         Returns a match where the specified characters are at the beginning or at the end of a word
(the          "r" in the beginning is making sure that the string is being treated as a "raw string")	        r"\bain"

r"ain\b"	

\B	         Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
             (the "r" in the beginning is making sure that the string is being treated as a "raw string")	   r"\Bain"r"ain\B"	

\d	         Returns a match where the string contains digits (numbers from 0-9)	                           "\d"	
\D	         Returns a match where the string DOES NOT contain digits	                                       "\D"	
\s	         Returns a match where the string contains a white space character	                               "\s"	
\S	         Returns a match where the string DOES NOT contain a white space character	                       "\S"	
\w	         Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	         Returns a match where the string DOES NOT contain any word characters	                           "\W"	
\Z	         Returns a match if the specified characters are at the end of the string	                       "Spain\Z"
"""


# A set is a set of characters inside a pair of square brackets [] with a special meaning:
"""
Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""


import re
txt = "The rain in Spain"
#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 


import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


# The split() Function
import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# maxsplit
import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


# The sub() Function
import re
#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re
#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


# A Match Object is an object containing information about the search and the result.
import re
#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

import re
#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re
#The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


# Import re
import re
# Create a string
txt = "The rain in Spain"
# Search for "Spain"
x = re.search("Spain", txt)
# Print the span
print(x.span())