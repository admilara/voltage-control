# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:32:02 2025

@author: Lara Buljan
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create meshgrid of g and tan(phi)
g_vals = np.linspace(0.01, 5.0, 200)
tan_phi_vals = [0.0, 0.2, 0.5, 1.0, -0.2, -0.3, -0.4]

G, TAN_PHI = np.meshgrid(g_vals, tan_phi_vals)

# Compute v from equation (2.10)
V = 1 / np.sqrt(G**2 + (1 + G * TAN_PHI)**2)

# Compute p and q
P = V**2 * G
Q = P * TAN_PHI
S = np.sqrt(P**2 + Q**2)

# Mask out values where S > 1.0
mask = S <= 1.0
P_valid = P[mask]
Q_valid = Q[mask]
V_valid = V[mask]

# Plot in 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(P_valid, Q_valid, V_valid, c=V_valid, cmap='viridis', s=2)


#V_masked = np.where(S <= 1.0, V, np.nan)
#P_masked = np.where(S <= 1.0, P, np.nan)
#Q_masked = np.where(S <= 1.0, Q, np.nan)
#sc = ax.plot_surface(P_masked, Q_masked, V_masked, cmap='viridis', edgecolor='none')


ax.set_xlabel("Radna snaga $p$ (p.u.)")
ax.set_ylabel("Jalova snaga $q$ (p.u.)")
ax.set_zlabel("Napon $v$ (p.u.)")
ax.set_title("'Onion' površina: 3D veza između p, q i v")
fig.colorbar(sc, label='Napon $v$')

plt.tight_layout()
# change for different POV
#ax.view_init(elev=30, azim=135, roll=0)
#plt.show()
plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/onion-surface-pv.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)