print("Dame tres números: ")
n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))

if n1 < n2 and n1 < n3:
    if n2 < n3:
        print(f"{n1} {n2} {n3}")
    else: 
        print(f"{n1} {n3} {n2}")
else:
    if n2 < n1 and n2 < n3:
        if n1 < n3:
            print(f"{n2} {n1} {n3}")
        else:
            print(f"{n2} {n3} {n1}")
    else:
        if n3 < n1 and n3 < n2:
            if n1 < n2:
                print(f"{n3} {n1} {n2}")
            else:
                print(f"{n3} {n2} {n1}")