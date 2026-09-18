#  Shorthand If
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a=20
b=15
max_value = a if a>b else b 
print("The maximum value is:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)


# Logical Operators
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# not Operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Python evaluates not first, then and, then or

age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# Truth Tables
# and Operator
"""
Condition 1	Condition 2	Result
True	True	True
True	False	False
False	True	False
False	False	False
"""
# or Operator 
"""
Condition 1	Condition 2	Result
True	True	True
True	False	True 
False	True	True
False	False	False
"""

temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

username = "Tobias"                                   #"Tobias" ek non-empty string hai, isliye Python ise True maanta ha
password = "secret123"                                 #"secret123" → True
is_verified = True 
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

score = 85
if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")


# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Each level of nesting creates a deeper level of decision-making.
# The code evaluates from the outermost condition inward.

age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

age = 17
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

score = 85
attendance = 90
submitted = True
if score >= 80:
  if attendance >=75:
    if submitted:
      print("You passed the course !")
    else:
      print("Assignment not submittted")
  else:
    print("Attendance is too low ")
else:
  print("you fail ")

# Nested If vs Logical Operators
temperature = 25
is_sunny = True
if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True
if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

score = 92
extra_credit = 5
if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")


# Pass Statement
# if statements cannot be empty,
#  but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

# why?
"""
The pass statement is useful in several situations:
When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later
"""

age = 20
if age < 18:
  pass                      # TODO: Add underage logic later
else:
  print("Access granted")

# pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). 
# You need pass where Python expects a statement, not just a comment.

score = 85
if score > 80:
  pass  # This is excellent
print("Score processed")

# Multiple Conditions
# You can use pass in any branch of an if-elif-else statement.
value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass  # Zero case - no action needed
else:
  print("Positive value")

def calculate_discount(price):
  pass  # TODO: Implement discount logic
# Function exists but doesn't do anything yet


# code challenge:
# Create age variable
age = 20

# Write if/elif/else
if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")
