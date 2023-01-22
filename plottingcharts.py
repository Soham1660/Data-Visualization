import pandas as pd

df = pd.read_csv('main.csv')

mass = df['Mass'].tolist()
radius = df['Radius'].tolist()

simass=[]
for data in mass:
    mul = data*1.989e+30
    simass.append(mul)

siradius=[]
for data in radius:
    mul2 = data*6.957e+8
    siradius.append(mul2)

gravity=[]
G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)

df.to_csv("final.csv")

import matplotlib.pyplot as plt
plt.scatter(simass, siradius)
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.title('Mass vs Radius')
plt.show()

plt.scatter(simass, gravity)
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.title('Mass vs Gravity')
plt.show()