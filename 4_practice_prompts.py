
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,

m = "mouse"

k = "keyboard"

m1 = "monitor"
# Insert those variables into an f-string sentence(look at slide 22)in repl.it

print(f"In AP COMP I use a {m}, {k}, and {m1}.")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

name = "joaquin"

date = "October 28"

movie = "maze runner"

print(name)
print(date)
print(movie)

# Print your name and age on separate lines using a single print() function.

name = "joaquin"
age = 17

print(f"Name: {name}\nAge: {age}")

# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

print(f"In 10 years, {name} will be {age + 10} years old")
##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
print("Hello World")
name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value



#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary
blue_beetle_summary= "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
print(blue_beetle_summary)
# upper case the entire summary
print("Uppercase:", blue_beetle_summary.upper())
# print the summary
# print the summary in lowercase
print("Lowercase:", blue_beetle_summary.lower())
# replace the word blue with red
red_beetle_summary=  "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."
# print the summary 
print(red_beetle_summary)
# string index the word beetle and print it out
index_of_beetle = blue_beetle_summary.lower().index("beetle")
# print the last word of the summary
print("Last character:", red_beetle_summary[-1:5])  
# print the summary in reverse
print("reverse:", red_beetle_summary)


##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

learned_tdy = input("What are you learning today?")

print("You are learning:", learned_tdy)

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?

where_user_from = input("Where are you from?")

print("You are from:", where_user_from)

# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

f_name = input("What is your first name? ")
l_name = input("What is your surname? ")

print("Your name is", (f_name), (l_name))

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.
name = input("What is your name?")
color = input ("What is your favorite color?")

print("Your name is", (name), "and your favorite color is",(color))

