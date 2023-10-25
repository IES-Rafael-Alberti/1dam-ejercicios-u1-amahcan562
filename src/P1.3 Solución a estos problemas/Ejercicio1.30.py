"""PSEUDOCODIGO
Inicio
    Escribe "Introduce valor inicial: "
    Lee inicio
    Escribe "Introduce valor incremental: "
    Lee incremento
    Mientras (incremento <= 0) hacer
        Escribe "Introduce un valor mayor que 0: "
        Lee incremento
    Escribe "Introduce valor total: "
    Lee total
    Mientras (total <= 0) hacer
        Escribe "Introduce un valor mayor que 0: "
        Lee total
        
    Escribe "SERIE => 
    si (inicio <= total) entonces
        escribe inicio
        si (inicio != total) entonces
            Escribe "-"
        inicio += incremento
Fin
"""

inicio = int(input("Introduce valor inicial: "))
incremento = int(input("Introduce valor incremental: "))
while incremento <= 0:
    incremento = int(input("Introduce valor incremental  mayor que 0!!:"))
total = int(input("Introduce valor total: "))
while total <= 0:
    total = int(input("Introduce valor  mayor que 0:"))

print("SERIE => ",end="")
while inicio <= total:
    print(inicio,end="")
    if inicio != total:
        print("-",end="")
    inicio += incremento
