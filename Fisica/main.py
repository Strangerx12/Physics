import sympy as sp
import math
from enunciado import mostrar_enunciado
from masa1 import analizar_masa1
from masa2 import analizar_masa2

def pausar():
    input("\n👉 Presiona Enter para continuar al siguiente paso...")
    print("="*75)

def main():
    # 1. Presentación y esquema gráfico del problema
    mostrar_enunciado()
    pausar()

    # 2. Desglose analítico y visual del Bloque 1
    analizar_masa1()
    pausar()

    # 3. Desglose analítico y visual del Bloque 2
    analizar_masa2()
    pausar()

    print("                  PASO 3: RESOLUCIÓN ALGEBRAICA DEL SISTEMA")
    print("-" * 75)
    print("Combinamos las ecuaciones de movimiento de ambas masas:")
    print("  • Ecuación 1 (Bloque 1): T - f1 - m1*g*sin(θ1) = m1*a")
    print("  • Ecuación 2 (Bloque 2): m2*g*sin(θ2) - T - f2 = m2*a")
    print("\nResolviendo el sistema simultáneamente para la Aceleración (a) y Tensión (T)...")

    # Definir símbolos globales unificados
    m1, m2, g, theta1, theta2, mu, T, a = sp.symbols('m1 m2 g theta1 theta2 mu T a', positive=True)
    
    N1 = m1 * g * sp.cos(theta1)
    f1 = mu * N1
    eq1 = sp.Eq(T - f1 - m1 * g * sp.sin(theta1), m1 * a)
    
    N2 = m2 * g * sp.cos(theta2)
    f2 = mu * N2
    eq2 = sp.Eq(m2 * g * sp.sin(theta2) - T - f2, m2 * a)
    
    # Resolución analítica con SymPy (sistema genérico asumido)
    solucion = sp.solve((eq1, eq2), (a, T))
    
    print("\n" " FÓRMULAS GENERALES ")
    print("\n• Fórmula general de la Aceleración (a):")
    sp.pprint(sp.simplify(solucion[a]))
    
    print("\n• Fórmula general de la Tensión (T):")
    sp.pprint(sp.simplify(solucion[T]))
    print("="*75)

    # 4. MÓDULO DE SIMULACIÓN NUMÉRICA CON VALIDACIÓN FÍSICA RIGUROSA
    opcion = input("\n¿Deseas probar el simulador ingresando valores numéricos reales? (s/n): ").strip().lower()
    if opcion == 's':
        print("\n" + "-"*75)
        print("                  MÓDULO DE SIMULACIÓN NUMÉRICA")
        print("-" * 75)
        try:
            val_m1 = float(input("Ingresa la masa 1 en kg: "))
            val_m2 = float(input("Ingresa la masa 2 en kg: "))
            val_th1 = float(input("Ingresa el ángulo del plano 1 en grados: "))
            val_th2 = float(input("Ingresa el ángulo del plano 2 en grados: "))
            val_mu = float(input("Ingresa el coeficiente de fricción mu: "))
            val_g = 9.81

            th1_rad = math.radians(val_th1)
            th2_rad = math.radians(val_th2)

            # Componentes del peso paralelas a los planos
            F1 = val_m1 * val_g * math.sin(th1_rad)
            F2 = val_m2 * val_g * math.sin(th2_rad)
            
            # Normales y fuerzas de fricción cinética para cada bloque
            n1 = val_m1 * val_g * math.cos(th1_rad)
            n2 = val_m2 * val_g * math.cos(th2_rad)
            
            fk1 = val_mu * n1
            fk2 = val_mu * n2
            f_max_total = fk1 + fk2

            print("\n--- EVALUACIÓN ESTÁTICA Y DINÁMICA DEL MOVIMIENTO ---")
            print(f"   ► Fuerza paralela Bloque 1 (F1) = {F1:.2f} N")
            print(f"   ► Fuerza paralela Bloque 2 (F2) = {F2:.2f} N")
            print(f"   ► Fricción máxima total (f_total) = {f_max_total:.2f} N")

            # Determinamos fuerza motriz neta absoluta
            fuerza_motriz_neta = abs(F1 - F2)

            print("\n" " RESULTADOS DE LA SIMULACIÓN ")
            
            if fuerza_motriz_neta <= f_max_total:
                print("   [ESTADO]: El sistema NO SE MUEVE (En Reposo).")
                print("   ► Aceleración del sistema (a) = 0.0000 m/s²")
                
                # Tensión estática según qué bloque ejerza mayor tracción
                if F1 > F2:
                    t_estatica = F2 + fk2 # o equivalente por equilibrio
                else:
                    t_estatica = F1 + fk1
                print(f"   ► Tensión de la cuerda (T)     = {t_estatica:.4f} N")
            else:
                masa_total = val_m1 + val_m2
                print("   [ESTADO]: El sistema ESTÁ EN MOVIMIENTO.")
                
                # Aplicamos la dirección correcta según qué masa sea mayor
                if F1 > F2:
                    print("   [DIRECCIÓN]: La Masa 1 baja y la Masa 2 sube (F1 > F2).")
                    a_val = (F1 - F2 - fk1 - fk2) / masa_total
                    T_val_1 = F1 - fk1 - (val_m1 * a_val)
                    T_val_2 = F2 + fk2 + (val_m2 * a_val) # chequeo cruzado
                else:
                    print("   [DIRECCIÓN]: La Masa 2 baja y la Masa 1 sube (F2 > F1).")
                    a_val = (F2 - F1 - fk1 - fk2) / masa_total
                    T_val_1 = F2 - fk2 - (val_m2 * a_val)
                    T_val_2 = F1 + fk1 + (val_m1 * a_val) # chequeo cruzado

                print(f"   ► Aceleración del sistema (a) = {a_val:.4f} m/s²")
                print(f"   ► Tensión calculada (Bloque 1) = {T_val_1:.4f} N")
                print(f"   ► Tensión calculada (Bloque 2) = {T_val_2:.4f} N")

                # Verificación de consistencia entre ambas masas
                if abs(T_val_1 - T_val_2) < 1e-3:
                    print("   [VERIFICACIÓN]: ¡Consistencia de Tensión OK! Ambas masas coinciden ✔")
                else:
                    print("   [ALERTA]: ¡Advertencia! Las tensiones calculadas por ambos bloques difieren.")

            print("="*75)
        except Exception as e:
            print(f"Error en los datos ingresados: {e}")

if __name__ == "__main__":
    main()