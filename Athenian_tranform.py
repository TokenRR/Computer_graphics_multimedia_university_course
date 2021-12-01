import matplotlib.pyplot as plt
import math

arrX = []
arrY = []
a = 10*3*math.pi/180

f = open('DS6.txt', 'r')
for line in f:
    x = line[0:-1]
    c1, c2 = x.split(' ')
    arrX.append(int(c1))
    arrY.append(int(c2))
f.close()

for i in range(len(arrX)):
    arrX[i] -= 480
    arrY[i] -= 480

for i in range(len(arrX)):
    arrX[i] = arrX[i] * math.cos(a) + arrY[i] * math.sin(a)
    arrY[i] = arrX[i] * math.sin(a) + arrY[i] * math.cos(a)

for i in range(len(arrX)):
    arrX[i] += 480
    arrY[i] += 480

plt.figure(figsize=(12, 12))
plt.scatter(arrY, arrX)
plt.axis('off')
plt.savefig('saved_figure.png')
plt.show()