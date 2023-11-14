print("Introduce dos números: ")
n1 = float(input(""))
n2 = float(input(""))

opcion = 0
while opcion < 1 or opcion > 4:
    opcion = int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División):"))
    if opcion < 1 or opcion > 4:
        print("ERROR - No es una opción correcta (1-4)")

while opcion == 4 and n2 == 0:
    n2 = float(input("La división por cero no es posible.\nIntroduzca de nuevo el segundo número: "))
if opcion == 1:
    print(f"{n1} + {n2} = {+(n1+n2)}")
elif opcion == 2:
    print(f"{n1} - {n2} = {+(n1-n2)}")
elif opcion == 3:
    print(f"{n1} * {n2} = {+(n1*n2)}")
elif opcion == 4:
    print(f"{n1} / {n2} = {+(n1/n2)}")