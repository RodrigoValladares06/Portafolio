import numpy as np
from scipy.integrate import quad

def area_entre_curvas(r_ext, r_int, theta1, theta2):
    """
    Calcula el área entre dos curvas en coordenadas polares.
    r_ext: función r externa (mayor radio), definida como una función de theta
    r_int: función r interna (menor radio), definida como una función de theta
    theta1, theta2: límites de integración en radianes
    """
    def integrando(theta):
        return 0.5 * (r_ext(theta)**2 - r_int(theta)**2)
    
    area, _ = quad(integrando, theta1, theta2)
    return area

# Ejemplo: Área entre r = 3/2 y r = 1 - cos(theta)

def r_ext(theta):
    return 3/2

def r_int(theta):
    return 1 - np.cos(theta)

theta1 = 2*np.pi/3
theta2 = 4*np.pi/3

resultado = area_entre_curvas(r_ext, r_int, theta1, theta2)
print(f"Área entre las curvas: {resultado:.4f}")
