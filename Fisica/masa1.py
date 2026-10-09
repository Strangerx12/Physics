import sympy as sp
from dcl_plot import graficar_dcl

def analizar_masa1():
    print("\n" + "-"*75)
    print("                  PASO 1: ANÁLISIS DE LA MASA 1 (Bloque Izquierdo)")
    print("-"*75)
    
    print(" [🎨] Abriendo ventana con el Diagrama de Cuerpo Libre de la Masa 1...")
    graficar_dcl("m1") # <--- ESTA LÍNEA ES LA QUE DIBUJA EL DIAGRAMA
    
    m1, g, theta1, mu, T, a = sp.symbols('m1 g theta1 mu T a', positive=True)
    
    print(" [✔] Eje Y (Equilibrio perpendicular al plano):")
    print("     ΣFy1 = N1 - m1*g*cos(θ1) = 0")
    N1 = m1 * g * sp.cos(theta1)
    print(f"     => Despejando Normal: N1 = {N1}")
    
    print("\n [✔] Fuerza de Fricción:")
    f1 = mu * N1
    print(f"     => Ff1 = μ * N1  ==>  Ff1 = {f1}")
    
    print("\n [✔] Eje X (Movimiento paralelo al plano):")
    print("     ΣFx1 = T - Ff1 - m1*g*sin(θ1) = m1*a")
    
    eq1 = sp.Eq(T - f1 - m1 * g * sp.sin(theta1), m1 * a)
    return eq1