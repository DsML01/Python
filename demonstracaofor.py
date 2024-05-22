def main():
    n = int(input())

    for i in range(n):
        
        item = int(input())

        if(item > 0):
            if(item % 2 == 0):
                print("PAR POSITIVO")
            else:
                print("ÍMPAR POSITIVO")
                
        elif(item < 0):
            if(item % 2 == 0):
                print("PAR NEGATIVO")
            else:
                print("ÍMPAR NEGATIVO")

        else:
            print("NULO")

main()