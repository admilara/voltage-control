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
list_phi_2 = [1, 0.95, 0.9, 0.86]

data_plot = {'cosphi': [1, 0.95, 0.9, 0.86],
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
    
    #tan_phi = np.tan(np.arccos(phi))
    #q2_vals = p2_vals * tan_phi
    
    plt.plot(p2_vals, v2_vals, label=f"cos$\\phi$ = {phi}", linewidth=2, color=color)
    
    plt.plot(pmax,vmax, 'o', color=color)
    
    #plt.plot(q2_vals, v2_vals, linestyle="dashed", linewidth=2, color=color, alpha=0.6)
    
    xmax.append(pmax)
    ymax.append(vmax)
    
plt.plot(xmax, ymax, linestyle='dashed', color='gray')


plt.ylabel(r"Napon $v_2$ (p.u.)")
plt.xlabel(r"Radna snaga $p_2$ (p.u.)")
plt.title("PV krivulja za jednostavni primjer s 2 sabirnice")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.tight_layout()
plt.show()

#plt.savefig(
#    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/pv-curve-multiple-cos.svg",
#    format="svg",
#    dpi=300,
#    bbox_inches="tight",
#    facecolor="white"
#)

plt.figure(figsize=(6,6))
plt.figure(figsize=(6, 6))

for index, phi in enumerate(data_plot['cosphi']):
    v2_vals = np.linspace(0.0, 1.1, 5000)
    p_vals = p2(v2_vals, phi)

    # Calculate sin(delta)
    sin_delta = -p_vals * XL / (v1_ref * v2_vals)

    # Filter invalid sin(delta)
    valid = np.abs(sin_delta) <= 1
    v2_valid = v2_vals[valid]
    p_valid = p_vals[valid]
    sin_valid = sin_delta[valid]

    cos_delta = np.sqrt(1 - sin_valid**2)
    q_vals = (v1_ref * -v2_valid / XL) * cos_delta - (-v2_valid**2 / XL)
    
    dq_dv = np.gradient(q_vals, v2_valid)
    zero_cross_idx = np.argmin(np.abs(dq_dv))
    
    v2_zero = v2_valid[zero_cross_idx]
    q_zero = q_vals[zero_cross_idx]
    
    color = data_plot['colors'][index]
    plt.plot(v2_valid, q_vals, label=f"cos$\\phi$ = {phi}", linewidth=2, color=color)
    plt.plot(v2_zero, q_zero, 'X', markersize=8, markeredgecolor='black', color=color, label=f'dQ/dV=0 (cos$\\phi$={phi})')




plt.xlabel(r"Napon $v_2$ (p.u.)")
plt.ylabel(r"Jalova snaga $q_2$ (p.u.)")
plt.title("Q-V krivulje s označenim kritičnim točkama gdje je $dQ/dV_2 = 0$")
plt.grid(True)
plt.legend(fontsize='small', loc='best')
plt.xlim(left=0)
plt.tight_layout()


plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/qv-curve-multiple-cos.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)
