# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 14:48:17 2025

@author: Lara Buljan
"""

import numpy as np
import matplotlib.pyplot as plt

# Range of load admittances (g)
g_vals = np.linspace(0.01, 5, 1000)

# tan(phi) values for different power factors
tan_phi_values = [0.0, 0.2, 0.5, 1.0, -0.5, -0.2]  # 0 = unity, positive = inductive, negative = capacitive
colors = ['red', 'green', 'orange', 'blue', 'magenta', 'gold']

plt.figure(figsize=(10, 6))

critical_P = []
critical_V = []
counter=0

for tan_phi in tan_phi_values:
    P_list = []
    V_list = []
    
    for g in g_vals:
        v = 1 / np.sqrt(g**2 + (1 + g * tan_phi)**2)
        P = v**2 * g
        Q = P * tan_phi
        S = np.sqrt(P**2 + Q**2)
        
        if S <= 1.0 and P <= 1.0:
            P_list.append(P)
            V_list.append(v)
    
    P_arr = np.array(P_list)
    V_arr = np.array(V_list)
    
    idx_max = np.argmax(P_arr)
    P_crit = P_arr[idx_max]
    V_crit = V_arr[idx_max]

    critical_P.append(P_crit)
    critical_V.append(V_crit)
        
    if tan_phi > 0:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label = f"cos(φ) = {cos_phi} (ind.)"
    elif tan_phi < 0:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label = f"cos(φ) = {cos_phi} (kap.)"
    else:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label= f"cos(φ) = {cos_phi}"
        
    plt.plot(P_list, V_list, label=label, color=colors[counter])
    plt.plot(P_crit, V_crit, 'o', color=colors[counter])
    counter+=1

plt.plot(sorted(critical_P), sorted(critical_V), linestyle='dashed', color='gray')

# Plot formatting
plt.ylabel(r"Napon $v_2$ (p.u.)")
plt.xlabel(r"Radna snaga $p_2$ (p.u.)")
plt.title("PV krivulja za različite vrijednosti faktora snage cos(φ) (normalizirano)")
plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()

plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/pv-curve-multiple-cos-v2.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)
