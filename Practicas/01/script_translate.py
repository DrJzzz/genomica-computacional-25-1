# Integrantes del equipo:
# - Frida Zayuli Garcí Barquero
# - Menchaca Carrillo Rodolfo Josué
# - Ricardo Flores Mata

codones_traduccion = {"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", # Alanina
    # Cisteina
    "UGU":"C", "UGC":"C",
    # Acido aspartico
    "GAU":"D", "GAC":"D",
    # Acido glutamico
    "GAA":"E", "GAG":"E",
    # Fenilalanina
    "UUU":"F", "UUC":"F",
    # Glicina
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    # Histidina
    "CAU":"H", "CAC":"H",
    # Isoleucina
    "AUA":"I", "AUU":"I", "AUC":"I",
    # Lisina
    "AAA":"K", "AAG":"K",
    # Leucina
    "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    # Metionina
    "AUG":"M", 
    # Aspargina
    "AAU":"N", "AAC":"N",
    # Prolina
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    # Glutamina
    "CAA":"Q", "CAG":"Q",
    # Arginina
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
    # Serina
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S",
    # Treonina
    "ACU":"U", "ACC":"U", "ACA":"U", "ACG":"U",
    # Valina
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    # Triptofano
    "UGG":"W",
    # Tirosina
    "UAU":"Y", "UAC":"Y",
    # Stop
    "UAA":"_", "UAG":"_", "UGA":"_"}

def save_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        print("Error al guardar el archivo.")
        


def main():
    file_path = input("Ingresa el path al archivo fasta que deseas traducir: ")
    if not file_path:
        file_path = './p1_LosNucleotidos_gen1_F2.fasta'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            ### Crea y guarda el archivo de la cadena complementaria.
            cadena_complemento = content.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
            cadena_complemento = cadena_complemento.upper()
            
            save_to_file('./cDNA.fasta', cadena_complemento)
            
            ### Crea y guarda el archivo con mRNA correspondiente.
            mRNA = content.replace('T', 'U')
            
            save_to_file('./mRNA.fasta', mRNA)
            
            ### Crear y guardar el archivo con la secuencia de aminoácidos.
            protein_sequence = ""
            codon = ""
            for i in range(0, len(mRNA), 3):
                codon = mRNA[i:i+3]
                if codon in codones_traduccion:
                    protein_sequence += codones_traduccion[codon]
                else:
                    protein_sequence += "-"
            
            save_to_file('./aminoacidos.fasta', protein_sequence)
            
            
            print("Se han guardado los archivos correctamente.")
            
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except IOError:
        print("Error inesperado. >:(")

if __name__ == "__main__":
    main()