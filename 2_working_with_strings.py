
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello"
name = "World"

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"

# Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!

# Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!

# Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False

# Find the length of the string
print("Length of phrase:", len(phrase))  # Output: 14


declaration_of_independance = "all men are created equal, are endowed with unalienable rights including Life, Liberty and the pursuit of Happiness, and that governments derive their just powers from the consent of the governed to secure these rights"

print("Length of of DOI first paragraph:", len(declaration_of_independance))

# ----------------------------------------
# 3. Indexing and Slicing
# ----------------------------------------
chicago_mayor = "Johnson"
print(chicago_mayor[0])
print(chicago_mayor[6])
print(chicago_mayor[4])
print(chicago_mayor[4:])
print(chicago_mayor[0:4])
print(chicago_mayor[1:5])
# the first number is slicing is inclusive
# the second number is exclusive
# J,o,h,n,s,o,n
# 0,1,2,3,4,5,6
# when we get one character/letter its called indexing
# when we get a chunck of letters from a string its called slicing 

phrase3 = "Supercalifragilistic"

print(phrase3.upper())
cut = print(phrase3[0:5])
print(phrase3[5:9])
print(phrase3[19])

# Indexing: Access characters by position (0-based index)
print("First character:", phrase[0])  # Output: P
print("Last character:", phrase[-1])  # Output: !

# Slicing: Get a range of characters (start inclusive, end exclusive)
print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# Example combining everything:
print("Formatted Example:", (greeting + " " + name + "!").upper())
# Output: HELLO WORLD!


# ----------------------------------------
# 7. Strings: Advanced Concepts
# ----------------------------------------

# Creating Strings: use single or double quotes
greeting1 = 'Hello'
greeting2 = "Hi there"

# Printing Strings
print(greeting1)
print(greeting2)

# ----------------------------------------
# String Methods
# ----------------------------------------

sentence = "Python is fun to learn"

# .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)

# .format(): Allows inserting values into strings using {}
name = "Marvin"
age = 35
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# You can also use f-strings (Python 3.6+)
intro_fstring = f"My name is {name} and I am {age} years old."
print(intro_fstring)
