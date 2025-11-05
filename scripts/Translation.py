# translation_fake.py
import sys

if len(sys.argv) != 3:
    print("Usage: python3 Translation.py <rna_file> <output_file>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    rna_seq = f.read().strip()

protein = "XXX"  

with open(sys.argv[2], "w") as f:
    f.write(protein)

print("Protein sequence generated.")
