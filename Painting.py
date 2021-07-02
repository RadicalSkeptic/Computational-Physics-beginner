import numpy as np
from matplotlib import image, pyplot

img = image.imread("Downloads/myimage.jpg")

a = img.copy()
ds = 3
n = a.shape[0]
z = int(n/ds-ds+1)
k = np.zeros((n, n, 3))


def rf(r, i, j, ds):
    if r > 0:
        k[x*ds+i][y*ds+j][0] = 1
        return 1
    else:
        return 0


def gf(g, i, j, ds):
    if g > 0:
        k[x*ds+i][y*ds+j][1] = 1
        return 1
    else:
        return 0


def bf(b, i, j, ds):
    if b > 0:
        k[x*ds+i][y*ds+j][2] = 1
        return 1
    else:
        return 0


for x in range(z):
    if x % 10 == 0:
        print(x*100/z, '%')
    for y in range(z):
        vr = 0
        vg = 0
        vb = 0
        for i in range(ds):
            for j in range(ds):
                vr += a[x*ds+i][y*ds+j][0]
                vg += a[x*ds+i][y*ds+j][1]
                vb += a[x*ds+i][y*ds+j][2]
        v = vr+vg+vb
        r = vr*(ds**2)/v
        g = vg*(ds**2)/v
        b = vb*(ds**2)/v
        for i in range(ds):
            j = 0
            while j < ds:
                j += 1
                rnd = np.random.rand()
                if rnd <= .33:
                    delta = rf(r, i, j, ds)
                    if delta == 0:
                        j -= 1
                    else:
                        r -= 1
                elif rnd <= .66:
                    delta = gf(g, i, j, ds)
                    if delta == 0:
                        j -= 1
                    else:
                        g -= 1
                else:
                    delta = bf(b, i, j, ds)
                    if delta == 0:
                        j -= 1
                    else:
                        b -= 1

pyplot.imshow(k)
pyplot.show()
