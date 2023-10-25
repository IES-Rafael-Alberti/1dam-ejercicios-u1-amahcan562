peso = float(input("Introduce tu peso: "))
estatura = float(input("Introduce tu estatura en cm: "))

estatura /= 100
indice = peso / estatura**2

print("Tu índice de masa corporal es de",indice,".")