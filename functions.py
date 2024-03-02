#u can define the main function above everything and the other functions
#under it and when use the app, call the main function at the very bottom line
#in order to be able to use every single part of your code

def main():
    x = int(input("X = "))
    y = int(input("Y = "))

    print("X + Y = " ,sum(x, y))
    print("X squared is ", square(x))

    if is_even(x):
        print("X is Even")
    else:
        print("X is Odd")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def square(n):
    return n * n

#if you call the function without passing arguments, it's gonna use " name = "User" " by default
def hello(name = "user"):
    print(f"Hello, {name}")

#name = input("What's you name? ")

#hello()
    
def sum(x, y):
    z = x + y
    return z

main()

