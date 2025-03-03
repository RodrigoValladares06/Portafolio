import numpy as np
import sympy as sp

def calcular_integral():
    x = sp.Symbol('x')
    expr = input("Ingrese la función a integrar en términos de x: ")
    funcion = sp.sympify(expr)
    
    tipo = input("¿Integral definida? (s/n): ").strip().lower()
    if tipo == 's':
        a = float(input("Ingrese el límite inferior: "))
        b = float(input("Ingrese el límite superior: "))
        resultado = sp.integrate(funcion, (x, a, b))
    else:
        resultado = sp.integrate(funcion, x)
    
    print(f"Resultado: {resultado}")

def operaciones_matrices():
    print("Ingrese las dimensiones de la matriz (filas columnas): ")
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    print("Ingrese los elementos de la matriz fila por fila separados por espacios:")
    elementos = []
    for i in range(filas):
        fila = list(map(float, input().split()))
        elementos.append(fila)

    matriz = np.array(elementos)

    print("\nElija una operación:")
    print("1. Suma con otra matriz")
    print("2. Resta con otra matriz")
    print("3. Multiplicación por otra matriz")
    print("4. Determinante (solo cuadradas)")
    print("5. Inversa (solo cuadradas)")

    opcion = int(input("Opción: "))

    if opcion in [1, 2, 3]:
        print("Ingrese la segunda matriz con las mismas dimensiones:")
        elementos2 = []
        for i in range(filas):
            fila = list(map(float, input().split()))
            elementos2.append(fila)
        
        matriz2 = np.array(elementos2)

        if opcion == 1:
            resultado = matriz + matriz2
        elif opcion == 2:
            resultado = matriz - matriz2
        elif opcion == 3:
            resultado = np.dot(matriz, matriz2)

    elif opcion == 4:
        if filas == columnas:
            resultado = np.linalg.det(matriz)
        else:
            print("La matriz debe ser cuadrada.")
            return

    elif opcion == 5:
        if filas == columnas:
            resultado = np.linalg.inv(matriz)
        else:
            print("La matriz debe ser cuadrada.")
            return

    print(f"Resultado:\n{resultado}")

def main():
    while True:
        print("\nCalculadora:")
        print("1. Calcular integral")
        print("2. Operaciones con matrices")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            calcular_integral()
        elif opcion == 2:
            operaciones_matrices()
        elif opcion == 3:
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
