
N = int(input(" N:"))


soma_p = 0
soma_i = 0


for i in range(1, N + 1):
    if i % 2 == 0:
        soma_p += i
    else:
        soma_i += i

if soma_p > soma_i:
    resultado = "A soma dos pares é maior."
elif soma_i > soma_p:
    resultado = "A soma dos ímpares é maior."
else:
    resultado = "As somas são iguais."

print(f"Soma dos pares: {soma_p}")
print(f"Soma dos ímpares: {soma_i}")
print(resultado)
