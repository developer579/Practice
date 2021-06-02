import matplotlib.pyplot as plt

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

plt.title("Histgram")
plt.xlabel("value")
plt.ylabel("frequency")

plt.hist(data,bins=8,color="m")

plt.show()

import random

x = []
y = []

for i in range(100):
    x.append(random.uniform(0,50))
    y.append(random.uniform(0,50))

v = [-100,100,-100,100]
plt.axis(v)

plt.scatter(x,y,marker="x")
plt.show()

import random

data0 = []

for i in range(1000):
    data0.append(random.normalvariate(0,10))

plt.title("Histgram")

plt.hist(data0,bins=50)
plt.show()

import numpy as np

x = []
y1 = []
y2 = []

x = np.arange(-8,8,0.01)
y1 = (3*x)+5
y2 = x**2

plt.title("y=f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.plot(x,y1,label="y=3x+5")
plt.plot(x,y2,label="y=x^2")
plt.legend()
plt.show()