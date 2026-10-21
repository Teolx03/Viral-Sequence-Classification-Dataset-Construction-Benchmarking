# This code run on the Zhejiang University server
# Software required on the server : Kraken version 2.17.1, Python 3.6.8
# Files required on the server: Kraken database, all testing sets 


import subprocess
import time

# path of kraken2 database 
db_path = "/public/workspace/3230300361bit/kraken_db"

# path of input fasta file 
input_fasta = "/public/workspace/3230300361bit/kraken_db/TESTING_SET1_1000bp_labeled.fasta"

# output kraken result 
report_file = "TESTING_SET1.report"
output_file = "TESTING_SET1.kraken"

# function run kraken()
def run_kraken():
    cmd = [
        "kraken2",
        "--db", db_path,
        "--threads", "8",
        "--fasta-input",
        "--report", report_file,
        "--output", output_file,
        input_fasta,
    ]

    print("[INFO] Running Kraken2...")
    subprocess.run(cmd, check=True)
    print("[INFO] Kraken2 finished successfully!")


if __name__ == "__main__":
    start_time = time.time()  # Start timing

    run_kraken()

    end_time = time.time()    # End timing
    print(f"\nTotal running time: {end_time - start_time:.2f} seconds")

