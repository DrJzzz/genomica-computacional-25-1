from collections import Counter

## Ejercicio 5

sequencias = [
    "CGGAGACTTTTCCACTGTCGTCGGAGTAGTAAAATAACGGTACGTCTTAGTGTGCACCATCGACTCTTTGTATTGCTCGTTAGGGGTCGCAGCCTCTTGTTAAGCCGTAATGGGTGATCCCCGCTCGTGAAACGGTGCGATCCTGTGATCTGTCAGTATCGAAGGAGTGAAAAAGCGATTGCTAGCCGAGGCGTACCGTG",
    "CGGAGTCCCCCCCACCGCCGCCGGTGCTGCATATCTACGGCACGCCCCAGTGTGCACCATCGACTCTTTGTATTGCTCGTTAGGGGTCGCAGCCTCTTGTTAAGCCGTAATGGGTGATCCCCGCTCGTGAAACGGTGCGATCCTGTGATCTATTGATGTTAGCAACATAGCCGCATAGTTATTGATTACAATATCTTATA",
    "CGGAGTCCCCCCCACCGCCGCCGGTGCTGCATATCTACGGCACGCCCCAGCGCGCTCCACCGACCCCCCGCACCGCCCGCCAGGGGCCGCAGCCCCCCGCCATGCCGCTACGGGCGTCCCCCGCCCGCGATTCGGCGCGACCCCGCGACCCGCCTGCACCGTAGGAGCGTAATAGCGTCCGCCTGCCGAGGCGCACCGCG",
    "CCCTACCCGGCAGACCCCTCCACGCCCCCCCGTAGCACCGGAACCAGATCCGCGGAGCGGGGAGGGAGGCGGGGGGGGGAGGTCGGTCGGGGGTGGGGCGACAAGAGAGGAAACGGCAAGGGGAAGGGAGGAAAAGGAGTGGAACGGAGGATTCATAGTAACTTGCGAAACGCACACGAAATGTGAACCATCACTACCAG"
]

# Esperanza y variansa para distintas ventans
window = [3, 4, 5, 8, 10, 20, 25, 40, 50]

def frecuencias_por_ventana(seq: str, ventana: int):
    res = []
    l = 0
    r = ventana
    length_of_seq = len(seq)
    cero = {'C':0, 'G':0, 'A': 0, 'T':0}

    while r <= length_of_seq:
        temp = dict(cero)
        
        for i in seq[l:r]:
            temp[i] += 1
        
        res.append(temp)
        l += ventana
        r += ventana
    return res

def esperanza_por_ventana(seq: str, ventana: int):
    count = Counter(seq)
    return {k: (v * ventana)/len(seq) for k, v in count.items()}

def calcular_varianza(frecuencias, media):
    varianza = {'C':0, 'G':0, 'A': 0, 'T':0}
    for freq in frecuencias:
        for nucleotide in freq:
            varianza[nucleotide] += (freq[nucleotide] - media[nucleotide]) ** 2
    for nucleotide in varianza:
        varianza[nucleotide] /= len(frecuencias)
    return varianza


for seq in sequencias:
    for w in window:
        print(f"Secuencia: {seq[:10]}... Ventana: {w}")
        frecuencias = frecuencias_por_ventana(seq, w)
        esperanza = esperanza_por_ventana(seq, w)
        varianza = calcular_varianza(frecuencias, esperanza)
        print(f"Esperanza: {esperanza}")
        print(f"Varianza: {varianza}\n")