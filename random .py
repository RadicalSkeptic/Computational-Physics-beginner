import msvcrt
print("Press X to generate 10 pseudorandom numbers\nPress any other key to exit\n\n")
a = chr(ord(msvcrt.getch()))
n = 10
print("pressed", a)
while(a == 'x'):
    i = 0
    while(i <= 9):
        print(n)
        n = (57*n+1) % 256
        i += 1
    print("\n")
    a = chr(ord(msvcrt.getch()))
