import random
import math
import numpy as np
x = []
for i in range(10000):
	dongxu2 = random.randint(0,1)
	dongxu1 = random.randint(0,1)
	x.append(dongxu1 + dongxu2)
#----------------------------
X = set(x)
P = []
for i in X:
	P.append(x.count(i)/len(x))
print(P)
Ex = 0
for i in X:
	Ex = Ex + i*P[i]
print(Ex)
Varx = 0
for i in X:
	Varx = Varx + (i - Ex)*(i - Ex) * P[i]
print(Varx)
print("Do lech chuan: ",math.sqrt(Varx))
P1 = 0
for i in range(1,len(x)):
	P1 = P1 + x.count(i)
print(P1)