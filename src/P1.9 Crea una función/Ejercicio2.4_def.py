def temperatura():
    temp = float(input("Especifique la temperatura en ºF: "))
    resultado = (temp-32) * 5 / 9
    return resultado
    
print("El resultado es", temperatura() , "ºC")