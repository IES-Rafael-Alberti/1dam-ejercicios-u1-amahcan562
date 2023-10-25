preciofinal = float(input("Especifique el importe final:"))
preciosiniva = preciofinal / 1.1
ivapagado = preciofinal - preciosiniva
print("Ha pagado usted",ivapagado,"€ de IVA")
print("El importe sin iva sería de",preciosiniva,"€")
print(f"El IVA es {10}%, el importe sin IVA es {preciosiniva}.")