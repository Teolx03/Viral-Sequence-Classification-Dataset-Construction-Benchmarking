import os
import random
import time
from Bio import Entrez

# ============================
# CONFIG
# ============================

Entrez.email = "your_email@example.com"   # put real email

ACCESSION_FILE = "Bacteroidetes.seq"      # input file you already have
N_RANDOM = 3                              # how many to sample
OUTPUT_FASTA = "combined_bacteria.fasta"  # combined fasta output
NEW_SEQ_FILE = "Bacteroidetes(1).seq"     # file that SHOULD be created


# ============================
# LOAD ACCESSIONS
# ============================

def load_accessions(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]


# ============================
# SELECT RANDOM
# ============================

def choose_random(accs, n):
    if len(accs) <= n:
        print("⚠ Only a few IDs, will use all; no remaining IDs.")
        return accs, []
    selected = random.sample(accs, n)
    remaining = [x for x in accs if x not in selected]
    return selected, remaining


# ============================
# DOWNLOAD & COMBINE
# ============================

def download_and_combine(selected, out_fasta):
    with open(out_fasta, "w") as out:
        for acc in selected:
            print(f"\n⬇ Downloading {acc} ...")
            try:
                handle = Entrez.efetch(
                    db="nucleotide",
                    id=acc,
                    rettype="fasta",
                    retmode="text"
                )
                fasta = handle.read()
                handle.close()

                out.write(fasta.strip() + "\n")
                print(f"✔ Added {acc} to {out_fasta}")

                time.sleep(0.34)
            except Exception as e:
                print(f"❌ Failed to download {acc}: {e}")


# ============================
# SAVE REMAINING IDS
# ============================

def save_remaining(remaining, path):
    with open(path, "w") as f:
        for acc in remaining:
            f.write(acc + "\n")
    print(f"\n📁 Remaining IDs saved to: {path}")
    print(f"Remaining count: {len(remaining)}")


# ============================
# MAIN
# ============================

def main():
    print("Current working directory:")
    print("  ", os.getcwd())  # <- shows exactly where files are written

    # 1. Load
    all_ids = load_accessions(ACCESSION_FILE)
    print(f"\nTotal IDs loaded from {ACCESSION_FILE}: {len(all_ids)}")

    # 2. Random split
    selected, remaining = choose_random(all_ids, N_RANDOM)

    print("\n🎯 Selected IDs:")
    for s in selected:
        print("  -", s)

    # 3. Download & combine
    download_and_combine(selected, OUTPUT_FASTA)

    # 4. Save remaining IDs to NEW_SEQ_FILE
    save_remaining(remaining, NEW_SEQ_FILE)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()

