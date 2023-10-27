def total(horas, coste):
    total = horas*coste
    return total

horas1 = int(input("Horas de trabajo: "))
coste1 = float(input("Coste por hora: "))

print("Importe total: " + str(total(horas1, coste1)))