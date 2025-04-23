# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:39:52 2025

@author: larab
"""

import numpy as np
import matplotlib.pyplot as plt

# Motor parameters
Rr = 0.7402  # Ohm
Rs = 0.7384  # Ohm
Xr_H = 0.003045  # Henries
Xs_H = 0.003045  # Henries
Vrated = 400  # Volts
f = 50  # Hz
p = 2 * 2  # 2 pole pairs = 4 poles

# Convert reactance from Henries to Ohms: X = 2 * pi * f * L
Xr = 2 * np.pi * f * Xr_H
Xs = 2 * np.pi * f * Xs_H

# Synchronous speed in rpm and angular speed
ns = 120 * f / p  # synchronous speed in RPM
ws = 2 * np.pi * ns / 60  # synchronous angular speed in rad/s

# Define slip range from s=0.001 to s=1 (avoid s=0 to prevent division by zero)
s = np.linspace(0.001, 1, 500)

# Voltage levels as a fraction of Vrated
voltage_levels = [0.6, 0.7, 0.8, 0.9, 1.0]
torque_curves = {}

load_torque_pu = 0.2

V_full = Vrated
T_full = (3 * V_full**2 * Rr / s) / (ws * ((Rs + Rr / s)**2 + (Xs + Xr)**2))
T_base = np.max(T_full)

torque_curves = {}
for v_scale in voltage_levels:
    V = Vrated * v_scale
    numerator = 3 * V**2 * Rr / s
    denominator = ws * ((Rs + Rr / s)**2 + (Xs + Xr)**2)
    T = numerator / denominator
    T_pu = T / T_base  # normalize to per-unit
    torque_curves[f"V = {int(v_scale * 100)}%"] = T_pu

# brzina rotora
n_r = (1 - s) * ns

# Plotting
plt.figure(figsize=(10, 6))
for label, T_pu in torque_curves.items():
    plt.plot(n_r, T_pu, label=label)
plt.axhline(load_torque_pu, color='black', linestyle='--', linewidth=1.5, label='moment tereta')


# presjecista po krivuljama za zadani iznos konstantnog tereta
intersections = {}
for label, T_pu in torque_curves.items():
    indices = np.argwhere(np.diff(np.sign(T_pu - load_torque_pu))).flatten()
    slips = s[indices]
    speeds = n_r[indices]
    for i, speed in enumerate(speeds):
        rounded_speed = round(speed,3)
        rounded_slips = round(slips[i], 3)
        plt.plot(speed, load_torque_pu, 'x', color='black')
        intersections[label] = intersections.get(label, []) + [(rounded_speed, rounded_slips)]

intersection_currents = {}

for label, points in intersections.items():
    v_percent = int(label.split('=')[1].strip('%'))
    V = Vrated * (v_percent / 100)
    for speed, slip in points:
        Z_eq = np.sqrt((Rs + Rr / slip)**2 + (Xs + Xr)**2)
        I = V / Z_eq
        intersection_currents[label] = intersection_currents.get(label, []) + [(speed, slip, round(I,3))]

plt.title("Moment vs brzina rotora za različite iznose napona (p.u.)")
plt.xlabel("Brzina rotora (o/min)")
plt.ylabel("Moment (p.u.)")
plt.xlim((0, 1600))
plt.ylim((0, 1.2))
plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()

plt.savefig("torque_voltage_recache.png", format='png', dpi=300)

print(intersection_currents)
print(intersections)

