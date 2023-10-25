""" PSEUDOCÓDIGO.
Inicio
    Lee n1
    Lee n2
    
    Si (n2 == n1) entonces
        Escribe "ERROR: Los numeros no pueden ser iguales!"
    sino    
        Si (n1<n2) entonces
            diferencia = n2-n1
            Escribe "El número menor es el n1 y entre ellos existen diferencia números enteros"
        sino
            diferencia = n1-n2
            Escribe "El número menor es el n2 y entre ellos existen diferencia números enteros"
Fin
"""

n1 = int(input("Introduzca un número: "))
n2 = int(input("Introduzca otro: "))

if n1 == n2:
    print("ERROR: Los numeros no pueden ser iguales!")
else:
    if n1<n2:
        diferencia = n2-n1
        print("El número menor es el",n1,"y entre ellos existen",diferencia,"números enteros")
    else:
        diferencia = n1-n2
        print("El número menor es el",n2,"y entre ellos existen",diferencia,"números enteros")
    