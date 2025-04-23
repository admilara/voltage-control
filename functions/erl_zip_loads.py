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
t_eval = np.linspace(*t_span, 600)
V_dip = 0.7

# Updated base values for realism
P0 = 0.8  # Active power (p.u.)
Q0 = 0.6  # Reactive power (p.u.)

# ZIP coefficients
alpha1, alpha2, alpha3 = 0.2, 0.3, 0.5
beta1, beta2, beta3 = 0.2, 0.3, 0.5

# ZIP-based static targets
def P_zip_func(V): return P0 * (alpha1 * V**2 + alpha2 * V + alpha3)
def Q_zip_func(V): return Q0 * (beta1 * V**2 + beta2 * V + beta3)

P_static_target = P_zip_func(V_dip)
Q_static_target = Q_zip_func(V_dip)

# Time constants
Tp = 2.0
Tq = 3.0

# Initial state
y0 = [P0, Q0]

# Define the ERL system of ODEs
def erl_ode_zip_realistic(t, y):
    P, Q = y
    dP_dt = (P_static_target - P) / Tp
    dQ_dt = (Q_static_target - Q) / Tq
    return [dP_dt, dQ_dt]

# Solve ODE
# Plot the updated ERL vs ZIP chart with voltage drop illustration like the figure user showed

# Recalculate P and Q ERL with proper values for plotting
sol = solve_ivp(erl_ode_zip_realistic, t_span, y0, t_eval=t_eval)
P_erl = sol.y[0]
Q_erl = sol.y[1]
P_zip = np.full_like(t_eval, P_static_target)
Q_zip = np.full_like(t_eval, Q_static_target)

# Extend time axis for voltage plot
t_voltage = np.linspace(-2, 10, 600)
V_voltage = np.where(t_voltage < 0, 1.0, V_dip)

# Plot everything together
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot ERL curves
ax1.plot(t_eval, P_erl, label="ERL Active Power (P)", color="orange", linewidth=2)
ax1.plot(t_eval, Q_erl, label="ERL Reactive Power (Q)", color="orangered", linewidth=2)

# Plot ZIP curves
ax1.plot(t_eval, P_zip, 'r--', label="ZIP Active Power (P)", linewidth=2)
ax1.plot(t_eval, Q_zip, 'm--', label="ZIP Reactive Power (Q)", linewidth=2)

# ERL recovery period
ax1.axvspan(0, 10, color='lightgray', alpha=0.3, label='ERL Recovery Period')

# Voltage dip line
ax1.axvline(0, color='red', linestyle='--', linewidth=1.5)
ax1.text(0.2, 0.95, "Voltage Dip to 0.7 p.u.", color='red')

# Plot voltage on a secondary axis
ax2 = ax1.twinx()
ax2.plot(t_voltage, V_voltage, color='black', linestyle='dotted', label="Voltage (V)", linewidth=2)
ax2.set_ylabel("Voltage (p.u.)", color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# Labeling
ax1.set_title("Comparison: ERL vs ZIP Load Power Response with Voltage Step")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Power (p.u.)")
ax1.grid(True)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="lower right")

plt.tight_layout()
plt.show()
