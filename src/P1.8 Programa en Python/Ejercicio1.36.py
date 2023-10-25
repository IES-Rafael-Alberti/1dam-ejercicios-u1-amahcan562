total = int(input("Cuántas notas vas a introducir? "))

while total < 1 or total > 100:
    print("ERROR - El número de notas debe ser un número entre 1 y 100")
    total = int(input("Cuántas notas vas a introducir? "))

print(f"Dame las {total} notas del curso: ")

media= 0
cont = 1
while cont <= total:
    nota = float(input(""))
    media = media + nota
    cont = cont + 1

media = media / total

print(f"La media es {media}")