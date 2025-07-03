# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 12:02:43 2025

@author: larab
"""

import numpy as np
import matplotlib.pyplot as plt


XL=0.1
v1_ref = 1.0
#phi2_deg = 30
#phi2 = np.radians(phi2_deg)

list_phi = [1, 0.98, 0.95, 0.93, 0.90, 0.88, 0.85]

data_plot = {'cosphi': [1, 0.98, 0.95, 0.93, 0.90, 0.88, 0.85],
             'colors': ['red', 'green', 'lightblue', 'lightsalmon', 'pink', 'violet', 'gold']}

def p2(v2, phi):
    tan_phi2 = np.tan(np.arccos(phi))
    numerator = -tan_phi2 + np.sqrt(tan_phi2**2 - (1 -(v1_ref/v2)**2))
    denominator = 1 + tan_phi2**2
    return (v2**2/XL) * (numerator / denominator)

xmax = []
ymax = []
plt.figure(figsize=(6,6))
for index, phi in enumerate(data_plot['cosphi']):
    v2_vals = np.linspace(0.0, 1.0, 5000)

    valid = (v2_vals >= 0.001)

    v2_vals = v2_vals[valid]

    p2_vals = p2(v2_vals, phi)

    index_pmax = np.argmax(p2_vals)

    vmax = v2_vals[index_pmax]
    pmax = p2_vals[index_pmax]
    color = data_plot['colors'][index]
    plt.plot(p2_vals, v2_vals, label=f"cos$\\phi$ = {phi}", linewidth=2, color=color)
    
    plt.plot(pmax,vmax, 'o', color=color)
    xmax.append(pmax)
    ymax.append(vmax)
    
plt.plot(xmax, ymax, linestyle='dashed', color='gray')    
#plt.axhline(y=vmax, color="red", linestyle="dashed")

#plt.plot(pmax, vmax, "ro")
#    plt.text(pmax-0.05, vmax-0.025, f"({vmax:.3f}, {pmax:.3f})", 
#             fontsize=10, color='red', verticalalignment='center', horizontalalignment="right")

#    plt.fill_between(p2_vals, v2_vals, vmax, where=(v2_vals < vmax), 
#                 color='red', alpha=0.2, label='Nestabilno područje', 
#                 hatch = "/", linewidth=2)


plt.ylabel(r"Napon $v_2$ (p.u.)")
plt.xlabel(r"Radna snaga $p_2$ (p.u.)")
plt.title("PV krivulja za jednostavni primjer s 2 sabirnice")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.tight_layout()
#plt.show()

plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/pv-curve-multiple-cos.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

