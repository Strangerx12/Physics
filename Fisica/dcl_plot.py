import matplotlib.pyplot as plt

def graficar_dcl(masa_nombre):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax.axvline(0, color='gray', linestyle='--', linewidth=1)
    ax.plot(0, 0, 'ko', markersize=10, zorder=5)
    
    if masa_nombre == "m1":
        title = "Diagrama de Cuerpo Libre: Bloque m1 (Izquierdo)"
        ax.quiver(0, 0, 1.2, 1.2, angles='xy', scale_units='xy', scale=1, color='red', label='Tensión (T)', width=0.007)
        ax.quiver(0, 0, 0, 2.0, angles='xy', scale_units='xy', scale=1, color='blue', label='Normal (N)', width=0.007)
        ax.quiver(0, 0, -1.0, -1.0, angles='xy', scale_units='xy', scale=1, color='purple', label='Fricción (Ff)', width=0.007)
        ax.quiver(0, 0, 0, -2.5, angles='xy', scale_units='xy', scale=1, color='green', label='Peso (mg)', width=0.007)
    else:
        title = "Diagrama de Cuerpo Libre: Bloque m2 (Derecho)"
        ax.quiver(0, 0, -1.2, 1.2, angles='xy', scale_units='xy', scale=1, color='red', label='Tensión (T)', width=0.007)
        ax.quiver(0, 0, 0, 2.0, angles='xy', scale_units='xy', scale=1, color='blue', label='Normal (N)', width=0.007)
        ax.quiver(0, 0, 1.0, -1.0, angles='xy', scale_units='xy', scale=1, color='purple', label='Fricción (Ff)', width=0.007)
        ax.quiver(0, 0, 0, -2.5, angles='xy', scale_units='xy', scale=1, color='green', label='Peso (mg)', width=0.007)

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    
    print(f" [ℹ] Ventana abierta para el {title}. Cierra la ventana para continuar...")
    plt.show()