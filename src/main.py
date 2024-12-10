import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constantes du pendule
g = 9.81  # Accélération due à la gravité (m/s^2)
L = 1.0  # Longueur du pendule (m)
theta0 = np.pi / 4  # Angle initial (en radians)
omega0 = 0.0  # Vitesse angulaire initiale (rad/s)


# Équations du mouvement pour un pendule simple
def pendule(t, y, L, g=9.81):
    """
    Arguments:
    - t : le temps
    - y : vecteur contenant l'angle (theta) et la vitesse angulaire (omega)
    - L : longueur du pendule
    - g : accélération due à la gravité

    Retourne:
    - dydt : dérivées du vecteur [theta, omega]
    """
    theta, omega = y
    if np.abs(theta) > 100 * np.pi:
        raise ValueError("L'angle dépasse la plage attendue.")
    dydt = [omega, -(g / L) * np.sin(theta)]
    return dydt


# Résolution numérique de l'équation différentielle
t_span = (0, 10)  # Intervalle de temps (0 à 10 secondes)
y0 = [theta0, omega0]  # Conditions initiales [angle, vitesse angulaire]
t_eval = np.linspace(t_span[0], t_span[1], 500)  # Points de temps pour évaluation

# Intégration de l'EDO
sol = solve_ivp(pendule, t_span, y0, t_eval=t_eval, args=(L, g))

# Extraire les résultats de la solution
t = sol.t
theta = sol.y[0]
omega = sol.y[1]

# Calcul de la position du pendule dans le plan (x, y)
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Trajectoire du pendule
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Trajectoire du pendule")
plt.title("Trajectoire d'un pendule simple")
plt.xlabel("Position horizontale (m)")
plt.ylabel("Position verticale (m)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.show()

# Animation du mouvement du pendule
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-L - 0.1, L + 0.1)
ax.set_ylim(-L - 0.1, L + 0.1)
(line,) = ax.plot([], [], "o-", lw=2)


# Fonction pour l'animation
def animate(i):
    line.set_data([0, x[i]], [0, y[i]])
    return (line,)


from matplotlib.animation import FuncAnimation

ani = FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)
plt.title("Animation du Pendule Simple")
plt.show()

# Affichage de l'énergie du système
kinetic_energy = 0.5 * (L * omega) ** 2  # Énergie cinétique
potential_energy = g * L * (1 - np.cos(theta))  # Énergie potentielle
total_energy = kinetic_energy + potential_energy  # Énergie totale

# Graphique de l'énergie
plt.figure(figsize=(8, 6))
plt.plot(t, total_energy, label="Énergie totale")
plt.plot(t, kinetic_energy, label="Énergie cinétique")
plt.plot(t, potential_energy, label="Énergie potentielle")
plt.title("Énergie du Pendule Simple")
plt.xlabel("Temps (s)")
plt.ylabel("Énergie (Joules)")
plt.legend()
plt.grid(True)
plt.show()
