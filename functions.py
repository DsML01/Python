#u can define the main function above everything and the other functions
#under it and when use the app, call the main function at the very bottom line
#in order to be able to use every single part of your code

def main():
    x = int(input("X = "))
    y = int(input("Y = "))

    print(sum(x, y))




#if you call the function without passing arguments, it's gonna use " name = "User" " by default
def hello(name = "user"):
    print(f"Hello, {name}")

#name = input("What's you name? ")

#hello()
    
def sum(x, y):
    z = x + y
    return z

main()

