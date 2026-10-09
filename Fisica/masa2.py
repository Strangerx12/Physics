import sympy as sp
from dcl_plot import graficar_dcl

def analizar_masa2():
    print("\n" + "-"*75)
    print("                  PASO 2: ANÁLISIS DE LA MASA 2 (Bloque Derecho)")
    print("-"*75)
    
    print(" [🎨] Abriendo ventana con el Diagrama de Cuerpo Libre de la Masa 2...")
    graficar_dcl("m2") # <--- ESTA LÍNEA ES LA QUE DIBUJA EL DIAGRAMA
    
    m2, g, theta2, mu, T, a = sp.symbols('m2 g theta2 mu T a', positive=True)
    
    print(" [✔] Eje Y (Equilibrio perpendicular al plano):")
    print("     ΣFy2 = N2 - m2*g*cos(θ2) = 0")
    N2 = m2 * g * sp.cos(theta2)
    print(f"     => Despejando Normal: N2 = {N2}")
    
    print("\n [✔] Fuerza de Fricción:")
    f2 = mu * N2
    print(f"     => Ff2 = μ * N2  ==>  Ff2 = {f2}")
    
    print("\n [✔] Eje X (Movimiento paralelo al plano):")
    print("     ΣFx2 = m2*g*sin(θ2) - T - Ff2 = m2*a")
    
    eq2 = sp.Eq(m2 * g * sp.sin(theta2) - T - f2, m2 * a)
    return eq2
