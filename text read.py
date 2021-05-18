import numpy as p
with open(r"C:\Users\WindowsX\Desktop\Read.txt", 'r') as f:
    radius = int(f.read())
    print(p.pi*radius**2)
