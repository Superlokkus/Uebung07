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

print poly

plt.plot(np.arange(11),poly(np.arange(11)))
plt.show()





