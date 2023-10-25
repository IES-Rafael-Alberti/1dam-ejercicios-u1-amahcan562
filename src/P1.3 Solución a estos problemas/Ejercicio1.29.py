""" PSEUDOCÓDIGO.
Inicio
    Lee nombre
    Lee edad
    
    Si (nombre == "") entonces
        nombre = "Desconocido"
    Mientras (edad<0 or edad>125) hacer
        Escribe "Introduzca una edad entre 0 y 125"
        Lee edad
    diferencia = 125 - edad
    Escribe "Te llamas nombre y tienes edad años, te quedan aún diferencia años por cumplir."
Fin
"""
nombre = input("Introduzca su nombre: ")
edad = int(input("Introduzca su edad: "))

if nombre == "":
    nombre = "Desconocido"
while edad < 0 or edad > 125:
    edad = int(input("Introduzca una edad entre 0 y 125!: "))
diferencia = 125 - edad
print("Te llamas",nombre,"y tienes "+str(edad)+", te quedan aún",diferencia,"años por cumplir.")