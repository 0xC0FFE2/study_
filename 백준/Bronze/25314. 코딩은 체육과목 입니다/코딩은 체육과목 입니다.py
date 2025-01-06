byte = int(input(""))

while True:
    if (byte > 4):
        print("long",end=' ')
    else:
        print("long int",end=' ')
        break
    byte -= 4