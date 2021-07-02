import numpy as np
from matplotlib import image, pyplot

img = image.imread("C:\\Users\\WindowsX\\Downloads\\beach.jpg")
a = img.copy()
ds = 2
nx = a.shape[0]
ny = a.shape[1]
zx = int(nx/ds-ds+1)
zy = int(ny/ds-ds+1)
a = a[:, :, 0]
b = np.zeros((zx, zy))
k = .1

for x in range(zx):
    for y in range(zy):
        m = 0
        for i in range(ds):
            for j in range(ds):
                m += a[x*ds+i][y*ds+j]
        b[x][y] = m/(ds**2)
        b[x][y] = (2*b[x][y])/(1+np.exp(k*(255/2-b[x][y])))

b = b*255/np.max(b)

with open(r"C:\Users\WindowsX\Desktop\ASCII art.txt", 'w') as f:
    for x in range(zx):
        for y in range(zy):
            if b[x][y] < 65.75:
                f.write('00')
            elif b[x][y] < 127.5:
                f.write('11')
            elif b[x][y] < 191.25:
                f.write('..')
            else:
                f.write('  ')
        f.write('\n')

print(np.max(b))
pyplot.imshow(b, cmap='Greys_r')
pyplot.show()
