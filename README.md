#  Simulador de Física: Sistema de Dos Planos Inclinados y Polea

Este proyecto es un simulador físico interactivo desarrollado en **Python** que resuelve, desglosa y visualiza paso a paso un sistema mecánico compuesto por **dos bloques con masas ($m_1$ y $m_2$) situados sobre planos inclinados con fricción**, unidos por una cuerda ideal que pasa por una polea en la cúspide.

El programa combina **cálculo simbólico** (deducción algebraica de fórmulas generales) con **visualización gráfica** (esquemas y Diagramas de Cuerpo Libre interactivos) y un **módulo de simulación numérica** con validación de reposo/movimiento.

---

## 📁 Estructura del Proyecto

El código está organizado de forma modular para separar responsabilidades y facilitar su mantenimiento:

* **`main.py`**: Archivo controlador principal. Coordina la ejecución paso a paso, resuelve el sistema algebraicamente mediante `SymPy` y maneja la simulación numérica interactiva.
* **`enunciado.py`**: Módulo encargado de mostrar la descripción teórica y generar una ventana gráfica con el esquema visual general del sistema.
* **`masa1.py`**: Módulo analítico para el Bloque 1 ($m_1$). Plantea las sumatorias en los ejes $X$ e $Y$, calcula la normal y la fricción, y despliega su Diagrama de Cuerpo Libre.
* **`masa2.py`**: Módulo analítico para el Bloque 2 ($m_2$). Realiza el mismo desglose físico y matemático para el bloque derecho.
* **`dcl_plot.py`**: Fábrica gráfica que utiliza `Matplotlib` para trazar los vectores de fuerza (Tensión, Normal, Peso y Fricción) sobre ejes coordenados inclinados.

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto en tu computadora, asegúrate de tener instalado Python y las siguientes librerías externas de cálculo y gráficos:

```bash
pip install sympy matplotlib numpy
