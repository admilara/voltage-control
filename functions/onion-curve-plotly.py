# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:44:00 2025

@author: Lara Buljan
"""

import numpy as np
import plotly.graph_objects as go

# Meshgrid
g_vals = np.linspace(0.01, 5.0, 200)
tan_phi_vals = np.linspace(-2.0, 2.0, 200)
G, TAN_PHI = np.meshgrid(g_vals, tan_phi_vals)

# Calculate v, p, q
V = 1 / np.sqrt(G**2 + (1 + G * TAN_PHI)**2)
P = V**2 * G
Q = P * TAN_PHI
S = np.sqrt(P**2 + Q**2)

# Mask out invalid points
V_masked = np.where(S <= 1.0, V, np.nan)

# Make 3D surface plot
fig = go.Figure(data=[go.Surface(
    z=V_masked,
    x=P,  # x-axis: p
    y=Q,  # y-axis: q
    colorscale='Viridis',
    showscale=True,
    colorbar=dict(title="Voltage v")
)])

fig.update_layout(
    title="Interactive Onion Surface (p–q–v)",
    scene=dict(
        xaxis_title="Active power p (p.u.)",
        yaxis_title="Reactive power q (p.u.)",
        zaxis_title="Voltage v (p.u.)"
    ),
    height=700,
    margin=dict(l=0, r=0, b=0, t=50)
)

fig.write_html("test.html")