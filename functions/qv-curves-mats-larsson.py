# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 14:54:44 2025

@author: Lara Buljan
"""

import numpy as np
import matplotlib.pyplot as plt

# Range of load admittance values (g)
g_vals = np.linspace(0.01, 5.0, 5000)

# tan(phi) values (power factor angles)
tan_phi_values = [0.0, 0.2, 0.5, 1.0, -0.2, -0.3, -0.4]  # positive = inductive, negative = capacitive
colors = ['red', 'green', 'orange', 'blue', 'magenta', 'gold', 'violet']
plt.figure(figsize=(10, 6))

counter=0
for tan_phi in tan_phi_values:
    Q_list = []
    V_list = []

    for g in g_vals:
        v = 1 / np.sqrt(g**2 + (1 + g * tan_phi)**2)
        P = v**2 * g
        Q = P * tan_phi
        S = np.sqrt(P**2 + Q**2)

        if S <= 1.0 and abs(Q) <= 1.0:
            Q_list.append(Q)
            V_list.append(v)

    Q_arr = np.array(Q_list)
    V_arr = np.array(V_list)

    #dQ_dV = np.gradient(Q_arr, V_arr)
    #sign_change_idx = np.where(np.diff(np.sign(dQ_dV)))[0]


    if tan_phi > 0:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label = f"cos(φ) = {cos_phi} (ind.)"
    elif tan_phi < 0:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label = f"cos(φ) = {cos_phi} (kap.)"
    else:
        cos_phi=round(np.cos(np.arctan(tan_phi)),2)
        label= f"cos(φ) = {cos_phi}"
        
    plt.plot(V_list, Q_list, label=label, color=colors[counter])

    if tan_phi >= 0:
        idx = np.argmax(Q_arr)  # maximum Q (peak)
    else:
        idx = np.argmin(Q_arr)  # minimum Q (valley)
    plt.plot(V_arr[idx], Q_arr[idx], 'x', color=colors[counter], markersize=8)
    counter+=1

# Plot formatting
plt.title("Q–V krivulje za različite vrijednosti faktora snage cos(φ) (normalizirano)")
plt.xlabel("Napon $v_2$ (p.u.)")
plt.ylabel("Jalova snaga $q_2$ (p.u.)")
plt.grid(True)
plt.legend(fontsize='small', loc='best')
plt.tight_layout()
#plt.show()

plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/qv-curve-multiple-cos-v2.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)