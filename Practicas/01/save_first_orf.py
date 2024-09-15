# Description: Script that reads a DNA sequence from a file 
# and saves the first ORF found in the sequence to another file.

import re

orf_regex = re.compile('ATG([ATGC]{3})+?T(AA|AG|GA)')

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def find_first_orf(content):
    match = orf_regex.search(content)
    return match.group(0) if match else None

def save_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

print(find_first_orf(read_file('./DNAseq/fragment_2.fna')))

def main():
    input_file_path = './DNAseq/fragment_2.fna'
    output_file_path = './p1_nombreEquipo_gen1_F2.fasta'
    
    first_orf = find_first_orf(read_file(input_file_path))
    save_to_file(output_file_path, first_orf)

if __name__ == "__main__":
    main()
        