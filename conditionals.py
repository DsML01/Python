x = int(input("X = "))

y = int(input("Y = "))

if (x < y):
    print("X is less than Y")

elif (x > y): 
    print("Y is less than X")

else:
    print("X is equal to Y")

if x < y or x > y:
    print("X is not equal to Y")

if x > y and y < x:
    print("x greater than y")