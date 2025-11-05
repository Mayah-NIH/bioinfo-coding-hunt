# transcription_fake.py
import sys

if len(sys.argv) != 3:
    print("Usage: python3 Transcription.py <dna_file> <output_file>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    data = f.read().strip()

with open(sys.argv[2], "w") as f:
    f.write(data)

print("Copied DNA to output file.")
