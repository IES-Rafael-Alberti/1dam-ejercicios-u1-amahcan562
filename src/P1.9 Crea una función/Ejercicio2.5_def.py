def importe(preciosiniva, iva):
    preciofinal = preciosiniva * iva
    print("El resultado es", importe(precionoiva, tipoiva), "€")
    return preciofinal

precionoiva = float(input("Especifique el precio sin IVA: "))
tipoiva = int(input("Escribe el porcentaje de IVA: "))