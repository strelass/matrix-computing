from random import random
import time

size = 10
a = [[[int(random() * size) for i in range(size)] for k in range(size)] for j in range(size)]
# a = [[[i for i in range(size)] for k in range(size)] for j in range(size)]
x = [0 for i in range(size)]
y = [0 for i in range(size)]
z = [0 for i in range(size)]


def main():
    print(a)
    for i in range(size):
        for k in range(size):
            tempx, tempy, tempz = 0, 0, 0
            for j in range(size):
                tempx += a[i][k][j]
                tempy += a[i][j][k]
                tempz += a[k][j][i]
            x[i], y[i], z[i] = tempx, tempy, tempz
    _max, _x, _y, _z = -1, -1, -1, -1
    for i, ei in enumerate(x):
        for k, ek in enumerate(y):
            for j, ej in enumerate(z):
                new = ei + ek + ej
                if _max < new:
                    _max = new
                    _x = i
                    _y = k
                    _z = j
    print(x)
    print(y)
    print(z)
    print("x: %s\ny: %s\nz: %s\nmax: %s" % (_x, _y, _z, _max))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
