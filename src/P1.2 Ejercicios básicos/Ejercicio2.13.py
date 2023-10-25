n = int(input("Introduce un número: "))
m = int(input("Introduce otro: "))

c = n // m
r = n % m
print("La división de {:.2f} entre {:.2f} da un cociente {:.2f} y un resto {:.2f}".format(n,m,c,r))
 