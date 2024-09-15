# Autores:
# - Josué Menchaca Carrillo 315294165
# - Ricardo Flores

import argparse
import re

orf_regex = re.compile('ATG([ATGC]{3})+?T(AA|AG|GA)')

def count_orfs(sequence):
    orfs = orf_regex.findall(sequence)
    return len(orfs)

def read_fna_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    parser = argparse.ArgumentParser(description="Process one or more .fna files.")
    parser.add_argument('input_files', type=str, nargs='+', help="Path(s) to the input .fna file(s)")
    args = parser.parse_args()

    for file_path in args.input_files:
        file_content = read_fna_file(file_path)
        orf_count = count_orfs(file_content)
        print(f"File: {file_path} - ORF Count: {orf_count}")
  
      
if __name__ == '__main__':
    main()
    