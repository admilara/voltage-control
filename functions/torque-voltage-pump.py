# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:51:01 2025

@author: larab
"""
# Re-import necessary modules after code state reset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Motor parameters
Rr = 0.7402  # Ohm
Rs = 0.7384  # Ohm
Xr_H = 0.003045  # Henries
Xs_H = 0.003045  # Henries
Vrated = 400  # Volts
f = 50  # Hz
p = 4  # 2 pairs of poles

# Convert reactances to Ohms
Xr = 2 * np.pi * f * Xr_H
Xs = 2 * np.pi * f * Xs_H

# Synchronous speed and angular speed
ns = 120 * f / p  # RPM
ws = 2 * np.pi * ns / 60  # rad/s

# Slip and rotor speed
s = np.linspace(0.001, 1, 500)
n_r = (1 - s) * ns

# Voltage levels to simulate
voltage_levels = [0.6, 0.7, 0.8, 0.9, 1.0]

# Define a non-linear load torque curve (fan/pump like: T_load ∝ n_r^2)
load_torque_pu = 0.5*(n_r / ns) ** 2  # Per unit torque
# Re-run the torque calculation loop with fixed T_base initialization
torque_curves = {}
T_base = None

# First calculate torque at full voltage to set the base
V_full = Vrated
T_full = (3 * V_full**2 * Rr / s) / (ws * ((Rs + Rr / s)**2 + (Xs + Xr)**2))
T_base = np.max(T_full)

# Now calculate torque curves at each voltage level
for v_scale in voltage_levels:
    V = Vrated * v_scale
    T = (3 * V**2 * Rr / s) / (ws * ((Rs + Rr / s)**2 + (Xs + Xr)**2))
    T_pu = T / T_base
    torque_curves[f"V = {int(v_scale * 100)}%"] = T_pu

# Plotting
plt.figure(figsize=(10, 6))
for label, T_pu in torque_curves.items():
    plt.plot(n_r, T_pu, label=label)

plt.plot(n_r, load_torque_pu, 'k--', linewidth=2, label="Moment tereta (pumpa)")

# Intersection calculations
intersection_data = []
for label, T_pu in torque_curves.items():
    diff = T_pu - load_torque_pu
    indices = np.argwhere(np.diff(np.sign(diff))).flatten()
    v_percent = int(label.split('=')[1].strip('%'))
    V = Vrated * (v_percent / 100)
    for idx in indices:
        slip_val = round(s[idx], 3)
        speed_val = round(n_r[idx], 3)
        torque_val = round(T_pu[idx], 3)
        Z_eq = np.sqrt((Rs + Rr / slip_val) ** 2 + (Xs + Xr) ** 2)
        current = round(V / Z_eq, 3)
        intersection_data.append({
            "Voltage Level": f"{v_percent}%",
            "Rotor Speed (RPM)": speed_val,
            "Slip": slip_val,
            "Torque (p.u.)": torque_val,
            "Current (A)": current
        })
        plt.plot(speed_val, torque_val, 'ro')

plt.title("Moment vs. brzina rotora za različite iznose napona i nelinearni teret")
plt.xlabel("Brzina rotora (o/min)")
plt.ylabel("Moment (p.u.)")
plt.xlim((0, 1600))
plt.ylim((0,1.2))
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()

plt.savefig(
    "torque-voltage-pump.jpg",
    format="jpg",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

print(intersection_data)
# Display results
#import ace_tools as tools; tools.display_dataframe_to_user(name="Motor-Load Intersections", dataframe=pd.DataFrame(intersection_data))
