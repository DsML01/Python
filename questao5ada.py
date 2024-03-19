def main():
    #1,5ml do produto para cada mil litros
    #mil litros == 1m³

    x = 3
    y = 5
    z = 1.7

    dose = 1.5

    volume = x * y * z

    litros = volume * 1000

    qtdml = (litros * 1.5)/1000

    print(qtdml)

main()