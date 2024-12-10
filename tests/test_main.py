import pytest
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constantes du pendule
g = 9.81  # Accélération due à la gravité (en m/s^2)
L = 1.0   # Longueur du pendule (en m)
theta0 = np.pi / 4  # Angle initial (en radians)
omega0 = 0.0  # Vitesse angulaire initiale (en rad/s)

# Fonction de mouvement du pendule
def pendule(t, y, L, g=9.81):
    theta, omega = y
    if L == 0:
        raise ZeroDivisionError("La longueur du pendule ne peut pas être nulle.")
    
    # Normalisation de l'angle dans l'intervalle [-pi, pi]
    theta = np.mod(theta + np.pi, 2 * np.pi) - np.pi
    
    dydt = [omega, -(g / L) * np.sin(theta)]
    return dydt

def test_initial_conditions():
    theta0 = np.pi / 4  # Angle initial
    omega0 = 0.0  # Vitesse angulaire initiale
    y0 = [theta0, omega0]
    L = 1.0  # Longueur du pendule

    # Résoudre l'EDO en utilisant une lambda pour passer L à pendulum
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol = solve_ivp(lambda t, y: pendule(t, y, L), t_span, y0, t_eval=t_eval)
    
    # Test des conditions initiales
    assert np.isclose(sol.y[0][0], theta0), f"Expected theta0 = {theta0}, got {sol.y[0][0]}"

# Test pour un pendule avec une longueur de pendule nulle

def test_zero_length():
    L = 0  # Longueur du pendule
    with pytest.raises(ZeroDivisionError):  # Division par zéro dans l'équation du mouvement
        pendule(0, [np.pi / 4, 0], L) 


# Test pour un angle trop grand
def test_large_angle():
    L = 1.0
    theta_large = 100 * np.pi  # Angle très grand
    omega0 = 0.0
    y0 = [theta_large, omega0]
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol = solve_ivp(pendule, t_span, y0, t_eval=t_eval, args=(L,))

    # Normaliser l'angle dans l'intervalle [-pi, pi]
    theta_normalized = np.mod(sol.y[0] + np.pi, 2 * np.pi) - np.pi

    # Vérifier si l'angle reste dans les limites attendues après l'intégration
    assert np.all(np.abs(theta_normalized) < 100 * np.pi), f"Angle exceeds expected range, got {theta_normalized[0]}"


# Test si une valeur non numérique pour l'angle lève une erreur
def test_invalid_angle():
    with pytest.raises(TypeError):
        pendule(0, ['invalid', 0])  # Angle non numérique

# Test pour vérifier la conservation de l'énergie
def test_energy_conservation():
    # Conditions initiales
    theta0 = np.pi / 4  # Angle initial
    omega0 = 0.0  # Vitesse angulaire initiale
    y0 = [theta0, omega0]
    
    # Résoudre l'EDO
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    sol = solve_ivp(pendule, t_span, y0, t_eval=t_eval, args=(L,))
    
    # Calcul de l'énergie cinétique, potentielle et totale
    kinetic_energy = 0.5 * (L * sol.y[1])**2  # Énergie cinétique
    potential_energy = g * L * (1 - np.cos(sol.y[0]))  # Énergie potentielle
    total_energy = kinetic_energy + potential_energy  # Énergie totale
    
    # Vérifier que l'énergie totale est presque constante
    energy_diff = np.max(np.abs(total_energy - total_energy[0]))
    assert energy_diff < 1e-1, f"Energy conservation violated, max difference {energy_diff}"

# Test pour une durée de simulation très longue (par exemple, 1000 secondes)
def test_long_simulation():
    theta0 = np.pi / 4  # Angle initial
    omega0 = 0.0  # Vitesse angulaire initiale
    y0 = [theta0, omega0]
    t_span = (0, 1000)
    t_eval = np.linspace(t_span[0], t_span[1], 5000)
    sol = solve_ivp(pendule, t_span, y0, t_eval=t_eval, args=(L,))
    
    assert sol.success, f"Simulation failed after long time: {sol.message}"

# Fonction principale de test
if __name__ == "__main__":
    pytest.main()
