# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:36:11 2025

@author: larab
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# === Parameters from Hill 1993 ===
V0 = 1.0      # Initial voltage
V1 = 0.8      # Voltage after step
t0 = 1.0      # Time of voltage drop
Tp = 2     # Recovery time constant
P_base = 0.8
y_p = -0.2

# ZIP coefficients
a_p, b_p, c_p = 0.3, 0.2, 0.5

# === Functions from the paper ===
def Ps(V): return P_base * (a_p * V**2 + b_p * V + c_p)
def kp(V): return y_p * V**2

# Voltage profile (step at t0)
def V_profile(t):
    return V0 if t < t0 else V1

# RHS of Hill’s equation: Ps(V) + kp(V)
def rhs(t, Pd):
    V = V_profile(t)
    return [(Ps(V) + kp(V) - Pd[0]) / Tp]

# Time vector
t_eval = np.linspace(0, 20, 2000)

# === Step-by-step build of the solution ===

# Pre-step: constant power before voltage drop
t_pre = t_eval[t_eval < t0]
Pd_pre = np.full_like(t_pre, Ps(V0))
V_pre = np.full_like(t_pre, V0)

# At t0: power jumps to Ps(V1) + kp(V0)
#P_jump = Ps(V1) + kp(V0)
P_jump = Ps(V1) + kp(V0)


# Post-step: solve the recovery ODE starting at t0
t_post = t_eval[t_eval >= t0]
sol = solve_ivp(rhs, [t0, t_eval[-1]], [P_jump], t_eval=t_post, method='RK45')
Pd_post = sol.y[0]
V_post = np.full_like(t_post, V1)

# Combine pre and post
t_all = np.concatenate([t_pre, t_post])
Pd_all = np.concatenate([Pd_pre, Pd_post])
V_all = np.concatenate([V_pre, V_post])

# === Plot ===
fig, axs = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

axs[0].plot(t_all, V_all, color='blue', linewidth=2)
axs[0].set_ylabel("Napon (p.u.)")
axs[0].set_title("a) Step promjena napona")
axs[0].grid(True)

axs[1].plot(t_all, Pd_all, color='red', linewidth=2)
axs[1].set_ylabel("Radna snaga Pd(t)")
axs[1].set_xlabel("Vrijeme(s)")
axs[1].set_title("b) Odziv radne snage")
axs[1].grid(True)

plt.tight_layout()


plt.savefig(
    "C:/Users/larab/Documents/GitHub/voltage-control/assets/gitbook/images/hill-voltage-response.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)