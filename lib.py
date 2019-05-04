import math
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro',color='b')
# plt.axis([0, 10, 0, 20])
# plt.show()

reta = [[], []]
circulo = [[], []]

def retaBresenhm(x1, y1, x2, y2,cor):
    x = x1
    y = y1
    p = 0
    dx = x2 - x1
    dy = y2 - y1
    xInc = 1
    yInc = 1
    if dx < 0:
        xInc = -1
        dx = -dx
    if dy < 0:
        yInc = -1
        dy = -dy
    if dy <= dx:
        p = dx / 2
        while x != x2:
            reta[0].append(x)
            reta[1].append(y)
            p -= dy
            if p < 0:
                y += yInc
                p += dx
            x += xInc
    else:
        p = dy / 2
        while y != y2:
            reta[0].append(x)
            reta[1].append(y)
            p += -dx
            if p < 0:
                x += xInc
                p += dy
            y += yInc
        reta[0].append(x)
        reta[1].append(y)

    print(reta)
    plt.plot(reta[0], reta[1], 'ro', color=cor)
    plt.show()

# retaBresenhm(-1, -9, -3, -6, 'r')

def circleBresenhm(posicaoCentroX, posicaoCentroY, raio, quantidadeDePontos, cor):

    distaciaEntrePontos = 2 * math.pi / quantidadeDePontos

    for c in range(0, quantidadeDePontos):
        cos = math.cos(c * distaciaEntrePontos)
        sin = math.sin(c * distaciaEntrePontos)

        x = int(cos * raio + posicaoCentroX)
        y = int(sin * raio + posicaoCentroY)

        circulo[0].append(x)
        circulo[1].append(y)

    print(circulo)
    plt.plot(circulo[0], circulo[1], 'ro', color=cor)
    plt.show()

plt.rcParams['figure.figsize'] = (15,15)
plt.ylim(50, 350, 0, 350)
plt.grid()
circleBresenhm(200, 200, 100, 100, 'g')

