import matplotlib.pyplot as plt

def mostrar_enunciado():
    print("="*75)
    print("          SIMULADOR FÍSICO: SISTEMA DE DOS PLANOS INCLINADOS")
    print("="*75)
    print(" [ℹ] Abriendo esquema visual gráfico del problema...")

    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Dibujar planos y polea
    ax.plot([0, 4, 4], [0, 2, 0], color='navy', lw=2)
    ax.plot([4, 4, 8], [0, 2, 0], color='navy', lw=2)
    ax.plot([0, 8], [0, 0], color='black', lw=2)
    
    polea = plt.Circle((4, 2), 0.25, color='gray', zorder=5)
    ax.add_patch(polea)
    
    ax.text(2.0, 1.3, "Bloque m1", fontsize=10, fontweight='bold', color='darkred', bbox=dict(boxstyle="round", fc="yellow", alpha=0.5))
    ax.text(5.3, 1.3, "Bloque m2", fontsize=10, fontweight='bold', color='darkred', bbox=dict(boxstyle="round", fc="yellow", alpha=0.5))
    ax.plot([2.3, 4, 5.7], [1.3, 2.25, 1.3], color='red', lw=1.5, ls='--')

    ax.set_xlim(-1, 9)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title("Esquema del Sistema: Dos Planos Inclinados y Polea", fontsize=12, fontweight='bold')
    
    print(" [ℹ] Cierra la ventana del esquema para continuar en la terminal...")
    plt.show() # Muestra la ventana y espera a que el usuario la cierre

    print("\nDescripción:")
    print("Se tienen dos bloques con masas (m1 y m2) situados sobre dos planos")
    print("inclinados con ángulos (theta1 y theta2), unidos por una cuerda ideal.")
    print("\n¿Qué hay que hallar paso a paso?")
    print("1. Las sumatorias de fuerzas en los ejes X e Y para cada masa.")
    print("2. Las fuerzas Normales (N) y de Fricción (Ff) de cada bloque.")
    print("3. La fórmula algebraica general de la Aceleración (a) y Tensión (T).")
    print("="*75)