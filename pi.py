
import os
def clear(): return os.system('cls')


x = 3.000000000000000000000000000000000000000000000000000000000000000
n = 0
while(n >= 0):
    x = x+((-1)**n)/((2*n**3)+(9*n**2)+(13*n)+6)
    print(n, "\n\n", x)
    clear()
    n += 1
