# Tarea 1.
# Implementaciones en python. 
# Genómica computacional.

import numpy as np
import re

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




