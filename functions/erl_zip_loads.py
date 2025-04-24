# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 15:04:22 2025

@author: larab
"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Time settings
t_span = (0, 20)
#t_eval = np.linspace(*t_span, 600)
t_full = np.linspace(-2, 20, 600)
V_dip = 0.7

# Updated base values for realism
P0 = 0.8  # Active power (p.u.)
Q0 = 0.6  # Reactive power (p.u.)

# ZIP coefficients
alpha1, alpha2, alpha3 = 0.2, 0.3, 0.5
beta1, beta2, beta3 = 0.2, 0.3, 0.5

P_pre = P0
Q_pre = Q0


# ZIP-based static targets
def P_zip_func(V): return P0 * (alpha1 * V**2 + alpha2 * V + alpha3)
def Q_zip_func(V): return Q0 * (beta1 * V**2 + beta2 * V + beta3)

P_post = P_zip_func(V_dip)
Q_post = Q_zip_func(V_dip)

P_zip_step = np.where(t_full<0, P_pre, P_post)
Q_zip_step = np.where(t_full<0, Q_pre, Q_post)


# Time constants
Tp = 2.0
Tq = 3.0

# Initial state
y0 = [P0, Q0]

# Define the ERL system of ODEs
def erl_ode_zip_realistic(t, y):
    P, Q = y
    dP_dt = (P_post - P) / Tp
    dQ_dt = (Q_post - Q) / Tq
    return [dP_dt, dQ_dt]

# Solve ODE
# Plot the updated ERL vs ZIP chart with voltage drop illustration like the figure user showed

# Recalculate P and Q ERL with proper values for plotting
erl_sol = solve_ivp(erl_ode_zip_realistic, t_span, y0, t_eval=t_full[t_full >= 0])
P_erl = np.concatenate([np.full_like(t_full[t_full < 0], P0), erl_sol.y[0]])
Q_erl = np.concatenate([np.full_like(t_full[t_full < 0], Q0), erl_sol.y[1]])

#P_erl = sol.y[0]
#Q_erl = sol.y[1]
#P_zip = np.full_like(t_eval, P_static_target)
#Q_zip = np.full_like(t_eval, Q_static_target)



# Extend time axis for voltage plot
V_voltage = np.where(t_full < 0, 1.0, V_dip)

# Plot everything together
fig, ax1 = plt.subplots(figsize=(12, 6))

# ERL curves
ax1.plot(t_full, P_erl, label="ERL radna (P)", color="orange", linewidth=2)
ax1.plot(t_full, Q_erl, label="ERL jalova (Q)", color="orangered", linewidth=2)

# ZIP corrected step curves
ax1.plot(t_full, P_zip_step, 'r--', label="ZIP radna (P)", linewidth=2)
ax1.plot(t_full, Q_zip_step, 'm--', label="ZIP jalova (Q)", linewidth=2)

# Shading recovery region
ax1.axvspan(0, 10, color='lightgray', alpha=0.3, label='ERL oporavak')

# Voltage step marker
#ax1.axvline(0, color='red', linestyle='--', linewidth=1.5)
#ax1.text(0.1, 0.3, "Voltage Dip to 0.7 p.u.", color='red')

# Voltage on secondary axis
ax2 = ax1.twinx()
ax2.plot(t_full, V_voltage, color='black', linestyle="dotted", label="Napon (p.u.)", linewidth=2)
ax2.set_ylabel("Napon (p.u.)", color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Labels and layout
ax1.set_title("ERL vs ZIP odziv snage tereta na promjenu napona")
ax1.set_xlabel("Vrijeme (s)")
ax1.set_ylabel("P,Q (p.u.)")
ax1.grid(True)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

plt.tight_layout()
ax1.set_xlim((-2,20))
#plt.show()

import matplotlib
matplotlib.use('Agg')

plt.savefig(
    "ERL-vs-ZIP.svg",
    format="svg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)