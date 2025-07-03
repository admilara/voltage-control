# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 09:58:29 2025

@author: larab
"""

import numpy as np
import matplotlib.pyplot as plt


XL=0.1
v1_ref = 1.0
phi2_deg = 30
phi2 = np.radians(phi2_deg)

def p2(v2):
    tan_phi2 = np.tan(np.arccos(0.86))
    numerator = -tan_phi2 + np.sqrt(tan_phi2**2 - (1 -(v1_ref/v2)**2))
    denominator = 1 + tan_phi2**2
    return (v2**2/XL) * (numerator / denominator)


v2_vals = np.linspace(0.0, 1.0, 5000)

valid = (v2_vals >= 0.001)

v2_vals = v2_vals[valid]

p2_vals = p2(v2_vals)

index_pmax = np.argmax(p2_vals)

vmax = v2_vals[index_pmax]
pmax = p2_vals[index_pmax]


plt.figure(figsize=(6,6))
plt.plot(p2_vals, v2_vals, label="PV krivulja", color='black', linewidth=2)

plt.axhline(y=vmax, color="red", linestyle="dashed")

plt.plot(pmax, vmax, "ro")
plt.text(pmax-0.05, vmax-0.025, f"({vmax:.3f}, {pmax:.3f})", 
         fontsize=10, color='red', verticalalignment='center', horizontalalignment="right")

plt.fill_between(p2_vals, v2_vals, vmax, where=(v2_vals < vmax), 
                 color='red', alpha=0.2, label='Nestabilno područje', 
                 hatch = "/", linewidth=2)


plt.ylabel(r"Napon $v_2$ (p.u.)")
plt.xlabel(r"Radna snaga $p_2$ (p.u.)")
plt.title("PV krivulja za jednostavni primjer s 2 sabirnice\nxL=0.1 p.u.cosphi=0.95")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.tight_layout()
#plt.show()

plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/pv-curve-example.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

