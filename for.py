n = int(input())

for i in range(n):
    x = int(input())

    if (x > 0):
        if (x % 2 == 0):
            print("PAR POSITIVO")
        else:
            print("ÍMPAR POSITIVO")

    elif(x < 0):
        if(x % 2 == 0):
            print("PAR NEGATIVO")
        else:
            print("ÍMPAR NEGATIVO")

    else:
        print("NULO")