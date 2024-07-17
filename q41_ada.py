n = int(input())

#primeira, segunda = valorprimeira, valorsegunda
pares, impares = 0, 0

for i in range(n):
    #print(i)
    if((i + 1) % 2 == 0): pares += (i + 1)
    else: impares += (i + 1)

print("A soma dos números ímpares é: ", impares)
print("A soma dos números pares é: ", pares)

if(pares > impares):
    print("A soma dos números pares é maior.")
if(impares > pares):
    print("A soma dos números pares é maior.")
if(pares == impares):
    print("A soma dos números pares e ímpares são iguais.")