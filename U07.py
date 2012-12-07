#!/usr/bin/python
# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt

"""Übung 07 Algebra mit numpy"""
#Markus Klemm WS12/13 Phy-BA

#Gegeben:
(x1,y1) = (-1.5,10.975)
(x2,y2) = (-0.4,13.008)
(x3,y3) = (1.9,0.843)
###
poly = np.poly1d(np.polyfit(np.array([x1,x2,x3]),np.array([y1,y2,y3]),2))

print "Berechnungen mit Polynom: " + str(poly)
print "Nullstellen: " + str(poly.r)

def LokaleExtrema(polynom):
    """Gibt die Koordinaten der lokalen Extrema des übergebenen Polynoms aus"""
    poly1 = np.polyder(polynom,1)
    poly2 = np.polyder(polynom,2)
    roots = poly1.r
    print roots
    for root in roots:
        if (poly2(root) <0):
            print "Lokales Maximum: " + str(root) + ";" + str(poly(root))
        elif (poly2(root) >0):
            print "Lokales Minimum: " + str(root) + ";" + str(poly(root))
        else:
            break
    
LokaleExtrema(poly)

plt.plot(np.linspace(-20,20),poly(np.linspace(-20,20)))
plt.show()





