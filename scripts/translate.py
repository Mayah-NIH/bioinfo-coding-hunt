# translate.py
import csv
import sys

if len(sys.argv) != 4:
    print("Usage: python3 translate.py <rna_file> <codon_table.csv> <output_protein_file>")
    sys.exit(1)

rna_file = sys.argv[1]
codon_file = sys.argv[2]
protein_file = sys.argv[3]

# Load codon table
codon_table = {}
with open(codon_file) as f:
    reader = csv.reader(f)
    for codon, aa in reader:
        codon_table[codon.upper()] = aa

with open(rna_file) as f:
    rna_seq = f.read().strip()

protein = ""
for i in range(0, len(rna_seq), 3):
    codon = rna_seq[i:i+3]
    protein += codon_table.get(codon, "")

with open(protein_file, "w") as f:
    f.write(protein)

print(f"Protein sequence written to {protein_file}")
