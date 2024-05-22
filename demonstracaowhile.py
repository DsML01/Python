def main():
    media = 0
    cont = 0

    while(1):
        item = int(input())
        
        if(item >= 0):
            media += item
            count += 1

        else:
            print(media/count)
            break



main()