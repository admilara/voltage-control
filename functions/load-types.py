# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 12:20:09 2025

@author: larab
"""

import numpy as np
from matplotlib import pyplot as plt

voltage = np.linspace(0, 1, 600)

constant_p = [1.0 for _ in voltage]
constant_i = voltage*1.0
constant_z = voltage**2 / 1.0

plt.figure(figsize=(10, 6))
plt.plot(voltage, constant_p, label="P=const.", color="black", linewidth=2, linestyle="dashdot")
plt.plot(voltage, constant_i, label="I=const.", color="blue", linewidth=2, linestyle="dashed")
plt.plot(voltage, constant_z, label="Z=const.", color="red", linewidth=2, linestyle="solid")

plt.title("karakteristike tereta - model konstantne snage, konstantne struje i konstantne impedancije")
plt.xlabel("Napon (p.u.)")
plt.ylabel("Radna snaga (p.u.)")
plt.xlim((0, 1.0))
plt.ylim((0,1.2))
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()

import matplotlib
matplotlib.use('Agg')

plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/ZIP-karakteristike.jpg",
    format="jpg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)