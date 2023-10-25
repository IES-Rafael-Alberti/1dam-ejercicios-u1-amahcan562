correo = input("Introduzca su correo: ")

nombre = correo.split("@") [0]
nuevo_correo = nombre + "@ceu.es"

print("El nuevo correo es",nuevo_correo)