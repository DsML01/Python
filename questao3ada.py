def main():
    javalandia = 52000
    pythonlandia = 74000

    taxa_crescimento_javalandia = 0.07
    taxa_crescimento_pythonlandia = 0.05

    cont = 0

    while javalandia < pythonlandia:

        javalandia += (javalandia * taxa_crescimento_javalandia)
        pythonlandia += (pythonlandia * taxa_crescimento_pythonlandia)
        #print(javalandia)
        #print(pythonlandia)

        cont += 1

    print(cont)

main()

