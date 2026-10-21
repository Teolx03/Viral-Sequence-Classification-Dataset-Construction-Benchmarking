from Bio import SeqIO


"""
   Split each sequence in input_fasta into fragments of length = window (default 1000 bp)
   Fragments shorter than the window size are discarded.
   All generated fragments are output to a fasta file 
 """


def split_fasta_by_window(input_fasta, window=1000):

    output_fasta = input_fasta.replace(".fasta", f"_{window}bp.fasta")

    with open(output_fasta, "w") as out:
        fragment_count = 0

        for record in SeqIO.parse(input_fasta, "fasta"):
            seq = str(record.seq)
            seq_len = len(seq)

            # 分割
            for i in range(0, seq_len - window + 1, window):
                fragment = seq[i:i+window]
                fragment_id = f"{record.id}_pos{i+1}_{i+window}"

                out.write(f">{fragment_id}\n{fragment}\n")
                fragment_count += 1

    print(f"[DONE] Output file: {output_fasta}")
    print(f"Total number of {window} bp fragments generated: {fragment_count}\n")
    return output_fasta



if __name__ == "__main__":
    # input file 
    input_file = "Testing_Cyanobacteria(6).fasta"   
    split_fasta_by_window(input_file)
