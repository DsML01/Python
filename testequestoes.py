# Lê o número de valores
N = int(input())

# Inicializa listas para armazenar os valores pares e ímpares
pares = []
impares = []

# Lê os valores e os classifica como pares ou ímpares
for _ in range(N):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Ordena os valores pares em ordem crescente
pares.sort()

# Ordena os valores ímpares em ordem decrescente
impares.sort(reverse=True)

# Imprime os valores pares
for par in pares:
    print(par)

# Imprime os valores ímpares
for impar in impares:
    print(impar)
