num = 3

total = int(input("Dime cuántos números debe tener la serie: "))

final = num * total
while num <= final:
    print(num,end="")
    if num < final:
        print(" ",end="")
    num = num + 3
