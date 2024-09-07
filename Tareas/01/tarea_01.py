# Tarea 1.
# Implementaciones en python. 
# Genómica computacional.

# importamos las dependencias.
import numpy as np

## Probabilidad y Estadística. ##
print("##Probabilidad y Estadística.##\n")

# Ejercicio 2
def misterio(M):
    i = 1
    D = 0
    while i < M:
        i += 1
        # Calcula numeros alatorios con dsitribución uniforme.
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        d = np.sqrt((x**2) + (y**2))
        if d <= 1:
            D += 1
    return 4 * (D / i)
print("Ejercicio 2: " + str(misterio(100000)) + "\n")

# Ejercicio 3
def expansion_modificacion(cadena, p):
    n = len(cadena)
    pos = np.random.uniform(0, 1)
    if pos <= p:
        icaracter = int(np.random.uniform(0, n - 1))
        mutacion =  "0" if cadena[icaracter] == "1" else "1"
        cadena = cadena[:icaracter] + mutacion + cadena[icaracter + 1:]
    else:
        cadena += cadena
    return cadena

def itera(cadena, n, p):
    for i in range(0, n):
        cadena += expansion_modificacion(cadena, p)
    return cadena
print("Ejercicio 3: " + itera("1", 10, 0.9))




