# combine multiple fasta file to one single output fasta


def combine_fasta_files(fasta_list, output_fasta):
    total = 0

    with open(output_fasta, "w") as outfile:
        for fasta in fasta_list:
            with open(fasta, "r") as f:
                for line in f:
                    outfile.write(line)
                    if line.startswith(">"):
                        total += 1

    print(f"[INFO] Combined FASTA written to: {output_fasta}")
    print(f"[INFO] Total sequences found (starting with '>'): {total}")


# input fasta file that need to combine 
fasta_files = [
    "Testing_Proteobacteria_5000bp(4737).fasta",
    "Testing_Firmicutes_5000bp(3238).fasta",
    "Testing_Actinobacteria_5000bp(921).fasta",
    "Testing_Bacteroidetes_5000bp(298).fasta",
    "Testing_Cyanobacteria_5000bp(60).fasta",
    "Testing_Spirochaetes_5000bp(50).fasta"
   ]
 
# output fasta file 
combine_fasta_files(fasta_files, "TESTING_SET5_labeled.fasta")
