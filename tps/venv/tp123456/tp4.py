# matplotlib

from random import *
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import axes3d

nombresAleatoires = []

counter = 0
while counter < 10:
    nombresAleatoires.append(randrange(10))
    counter += 1
    print(nombresAleatoires)

pyplot.plot(nombresAleatoires)
pyplot.ylabel("Nombres aléatoires")
pyplot.title("Courbe")
pyplot.show()

# question 5 Histogramme
pyplot.hist(nombresAleatoires, normed=1, facecolor='b')

# 3 4
courbe1 = []
courbe2 = []
courbe3 = []

counter = 0
while counter < 10:
    courbe1.append(randrange(0, 10))
    courbe2.append(randrange(10, 20))
    courbe3.append(randrange(20, 30))
    counter += 1

pyplot.title("3 Courbes aléatoires")
pyplot.ylabel("Chiffres aléatoires")
pyplot.xlabel("Numéro du chiffre")

pyplot.plot(range(10), courbe1, "y", linewidth=7)
pyplot.plot(range(10), courbe2, "b^")
pyplot.plot(range(10), courbe3, "r--")

pyplot.annotate('info', xy=(6, courbe3[6]), xytext=(5, courbe3[5] + 4),
                arrowprops={'facecolor': 'black', 'shrink': 0.03})
pyplot.show()

# Camembert
n = ['Admis', 'Redoublants', 'Rattrapages', 'Ajournés']
data = [35, 30, 25, 10]
pyplot.pie(data, labels=n, autopct='%1.1f%%')
pyplot.axis('equal')
pyplot.title('Résultat S09')
pyplot.show()

# 6
fig = pyplot.figure(figsize=(14, 6))

X = (-5, 5, 0.25)
Y = (-5, -5, 0.25)
Z = (-5, -5, 0.25)

axe = fig.add_subplot(1, 2, 2, projection='3d')
surface = axe.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

pyplot.show()
