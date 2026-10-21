from Bio import SeqIO

MANUAL_FILE = "sequence.fasta"
COMBINED_FILE = "combined_bacteria.fasta"

def extract_id(header):
    """
    Extract accession ID from FASTA header.
    Example:
        >NZ_CP103377.1 something something
    Returns:
        NZ_CP103377.1
    """
    return header.split()[0].lstrip(">")

# ============================
#  LOAD MANUAL SEQUENCE
# ============================

manual_record = next(SeqIO.parse(MANUAL_FILE, "fasta"))
manual_id = extract_id(manual_record.description)
manual_seq = str(manual_record.seq).upper()

print(f"📌 Manual file ID detected: {manual_id}")
print(f"Manual sequence length: {len(manual_seq)}")

# ============================
#  FIND THE SAME ID IN COMBINED FILE
# ============================

combined_seq = None

for record in SeqIO.parse(COMBINED_FILE, "fasta"):
    combined_id = extract_id(record.description)

    # match if combined ID starts with manual ID
    if combined_id.startswith(manual_id):
        combined_seq = str(record.seq).upper()
        break

if combined_seq is None:
    print(f"\n❌ ERROR: ID {manual_id} not found in {COMBINED_FILE}")
    exit()

print(f"Combined sequence length: {len(combined_seq)}")

# ============================
#  FULL NUCLEOTIDE COMPARISON
# ============================

if manual_seq == combined_seq:
    print("\n✅ PERFECT MATCH: All nucleotides identical.")
else:
    print("\n❌ Sequences differ!")

    # find mismatch
    min_len = min(len(manual_seq), len(combined_seq))

    for i in range(min_len):
        if manual_seq[i] != combined_seq[i]:
            print(f"\nFirst mismatch at position {i+1}:")
            print(f"  manual   : {manual_seq[i]}")
            print(f"  combined : {combined_seq[i]}")
            break
    else:
        print("\n⚠️ All positions match, but lengths are different.")
