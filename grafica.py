import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Función para calcular las coordenadas (x, y) en función del tiempo t
def calcular_coordenadas(t, velocidad_inicial, angulo):
    g = 9.8  # Aceleración debida a la gravedad
    radianes = np.deg2rad(angulo)
    x = velocidad_inicial * t * np.cos(radianes)
    y = velocidad_inicial * t * np.sin(radianes) - 0.5 * g * t**2
    return x, y

# Función de inicialización de la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización de la animación
def update(frame):
    x, y = calcular_coordenadas(frame * 0.05, velocidad_inicial, angulo)
    line.set_data(x, y)
    return line,

# Parámetros del movimiento parabólico
velocidad_inicial = 20  # en metros por segundo
angulo = 45  # en grados

# Configuración de la animación
fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)
line, = ax.plot([], [], 'o-', lw=2)

ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

plt.show()