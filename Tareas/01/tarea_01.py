# Tarea 1.
# Implementaciones en python. 
# Genómica computacional.

import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt

## Expresiones regulares. ##

print("##Expresiones regulares.##\n")

# Ejercicio 1

regex01 = re.compile('TATAG[^AT](T*|AC)TATA')

testSequences = ["TATACGCGTATAGAACTATAGCCCTATA",
                 "TATAGCGTATAGGACTATAGTATA",
                 "GTATGTATAGCCGACTTA",
                 "TATAGCCGACTATA"
                 ]

print("Resultado ejercicio 1: ")
for i in range(0, len(testSequences)):
    out = "La cadena " + str(i + 1)
    ans = regex01.search(testSequences[i])
    if ans:
        out = out + " contiene la expresión regular en la posición [" + str(ans.start()) + ", " + str(ans.end()) + "]"
    else:
        out += " no contiene la expresión regular."
    print(out)


# Ejercicio 2

regex_region_codificante = re.compile('ATG([ATGC]{3})*?T(AA|AG|GA)')

testSequences = ["ATATATACATACTGGTAATGGGCGCGCGTGTGTTAAGTTCTGTTGTAGGGGTGATTAGGGGCG",
                "GGCCCACACCCCACACCAATATATGTGGTGTGGGCTCCACTCTCTCGCGCTCGCGCTGGGGAT",
                "ATAAGGTGTGTGGGCGCGCCCCGCGCGCGCGTTTTTTCGCGCGCCCCCGCGCGCGCGCGCGCG",
                "GGCGCGGGACGCGGCGGCGGATCCCGATCCGTGCGTCAATACTATTATGGCCAGATAGAATAA",
                "GTGCTGCTGCGGCGCCCACACCTATTATCTCTCTCTCTCTGCCTCTCCACCTCGGGGCTTAAT",
                "GCGCTGCTGCTGGCTCGATGGGCGCGTGCGTCGTAGCTCGATGCTGGCTCGAGCTGTAATCTT",
                "GGCGCTCGCTCGGATGCGCGGCCGGGCTCTCTGCTCGCGCTCGCTTCGCGCTCGTGACCGCTG",
                "AATTGGTGCGCGCTCGCGCACACACAGAGAGAGGGTTTATATAGGATGATATATCCACATTGG",
                "ATGCTGCTGCTGGCTCTGCTTGCGCTCTGCTCGCTGGGGTGTGTGTGCCGCGCGCTGCTGCTC",
                "GCTGGGCTCGCTCGATGCGCGCGGGCGCGCGACCGCGGACGGCGTCGCTGCTAAATGGGCTTC"]
results = []
for i in range(0, len(testSequences)):
    if regex_region_codificante.search(testSequences[i]):
        results.append(i+1)

print("Resultado ejercicio 2: ")
print("Las cadenas que contienen la región codificante son: " + str(results) + "\n")
    

## Probabilidad y Estadística. ##
print("##Probabilidad y Estadística.##\n")

# Ejercicio 1

def leer_archivo(archivo_texto):
    try:
        list_lineas = []
        with open(archivo_texto, 'r') as archivo:
            for linea in archivo:
                list_lineas.append(linea.strip())
        return list_lineas
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except IOError:
        print("Ocurrió un error al leer el archivo.")

def contar_promotores(secuencia, promotores):
    conteo = {promotor : secuencia.count(promotor) for promotor in promotores}
    return conteo

def obtener_frame_data(secuencias):
    resultados = []
    promotores = ['AGATAG', 'TGATAG', 'AGATAA', 'TGATAA']
    for secuencia in secuencias:
        conteo = contar_promotores(secuencia, promotores)
        resultados.append(conteo)
    df_resultados = pd.DataFrame(resultados)
    df_resultados = df_resultados.fillna(0)
    return df_resultados

def botplox(df_resultados):
    plt.figure(figsize=(10, 6))
    df_resultados.boxplot()
    plt.title('Distribución de Apariciones de Promotores')
    plt.ylabel('Número de Apariciones')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def ejercico1(archivo):
    secuencias = leer_archivo("promotores.txt")
    df_resultados = obtener_frame_data(secuencias)
    # Descomentar si se quiere generar el botplox
    # botplox(df_resultados)
    # Media y desviación
    media = df_resultados.mean()
    desviacion_estandar = df_resultados.std()
    print("\nMedia de apariciones de cada promotor:\n" + str(media))
    print("\nDesviación estándar de apariciones de cada promotor:\n" + str(desviacion_estandar))

print("Ejercicio 1\n")
ejercico1("promotores.txt")

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

