# transcribe.py
import sys

if len(sys.argv) != 3:
    print("Usage: python3 transcribe.py <dna_file> <output_rna_file>")
    sys.exit(1)

dna_file = sys.argv[1]
rna_file = sys.argv[2]

with open(dna_file) as f:
    dna_seq = f.read().strip().upper()

rna_seq = dna_seq.replace("T", "U")

with open(rna_file, "w") as f:
    f.write(rna_seq)

print(f"RNA sequence written to {rna_file}")
