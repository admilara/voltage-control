# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 08:58:15 2025

@author: Lara Buljan
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_power_vs_voltage(phi_deg_list):
    """
    Plots active power P as a function of voltage V for a given power angle phi (in degrees).
    
    Args:
        phi_deg (float): Power factor angle phi in degrees.
    """
    # Given constants
    E = 1.0  # p.u.
    X = 0.1  # p.u.
    #phi_rad = np.radians(phi_deg)
    #tg_phi = np.tan(phi_rad)
    
    # Voltage range (avoid zero to prevent division by zero)
    V = np.linspace(0.01, 1.0, 500)
    
    plt.figure()
    
    for phi_deg in phi_deg_list:
        phi_rad = np.radians(phi_deg)
        tg_phi = np.tan(phi_rad)
    
        # Compute the expression under the square root
        sqrt_term = tg_phi**2 - (1 - (E**2) / (V**2))
        
        # Mask to avoid complex numbers and division by zero
        valid_mask = sqrt_term >= 0
        
        V_valid = V[valid_mask]
        sqrt_valid = np.sqrt(sqrt_term[valid_mask])
        
        numerator = -tg_phi + sqrt_valid
        denominator = 1 + tg_phi**2
    
        P = (V_valid**2) / X * (numerator / denominator)
    
        # Plotting
        #plt.figure()
        
        cos_phi = np.cos(np.deg2rad(phi_deg))
        cos_phi = round(cos_phi, 2)
        plt.plot(P, V_valid, label=f'cosφ = {cos_phi}°')
        
    plt.xlabel('Active Power P (p.u.)')
    plt.ylabel('Voltage V (p.u.)')
    plt.title('Active Power P vs Voltage V')
    plt.grid(True)
    plt.legend()
    plt.show()
    #plt.savefig(r"""C:\Users\larab\Documents\GitHub\voltage-control\assets\gitbook\images\pv-curve-example.svg""")

# Example usage with φ = 30 degrees
plot_power_vs_voltage([30,25,18])

