#name = input("Type your name here: ")
name = '     davi      '

#with this '+' I'm concatenating the string name with the string Hello,
print("Hello, " +name)

#here we take the '\n' out
print("Hello, ", end="")
print(name)

#this function take out the blank space from strings
name = name.strip()

#when u use ',' to declare the variables u gonna pass on prints
#it prints automatically a blank space " "
print("Hello,", name)

#this function, capitalize names
name = name.capitalize()

#here we take the space after use ',' to declare variables out
print("Hello, ", name, sep="")

name = 'davi silva'

#in this way, we can print variables directly on the print
print(f"Hello, {name}")

#We could use this
name = name.title()
print(f"Hello, {name}")

#if we want to use " " on our print, we should use ' ' one the print
print('Hello, "Davi"')

#or we can use it like this 
print("Hello, \"Davi\" ")

#we can use strip and title directly on the input (scanf)
name = input("What's your mom's name? ").strip().title()
print(f"Hello, {name}")

firstname, lastname = name.split(" ")

print(f"First name = {firstname}, Last name = {lastname}")

"""
That's a comment

a

a

a
"""