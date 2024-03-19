def main():
    i = 1
    max = 0

    for i in  range(10):
        a = int(input(" "))
        b = int(input(" "))
        c = int(input(" "))

        sum = a + b + c
      
        if (sum > max): max = sum
    
    print(max)

main()
