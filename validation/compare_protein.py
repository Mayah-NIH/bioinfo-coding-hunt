# compare_protein.py
import sys

if len(sys.argv) != 2:
    print("Usage: python3 compare_protein.py <protein_file>")
    sys.exit(1)

protein_file = sys.argv[1]

correct_protein = "MAIVMGR*KGAR*"  

with open(protein_file) as f:
    user_protein = f.read().strip()

# Hidden message as ASCII codes
secret_message = [77, 97, 114, 105, 97, 104, 32, 104, 97, 115, 32, 100, 101, 102, 114, 111, 115, 116, 101, 100, 44, 32, 77, 101, 114, 114, 121, 32, 67, 104, 114, 121, 115, 108, 101, 114]

if user_protein == correct_protein:
    # Convert ASCII to characters and print
    print(''.join(chr(i) for i in secret_message))
else:
    print("Protein does not match. Check your transcription/translation steps.")
