import csv
from pathlib import Path

# input kraken result 
REPORT_PATH = Path("TESTING_1000bp_18000.report")
KRAKEN_PATH = Path("TESTING_1000bp_18000.kraken")

# output analyzed kraken result
OUTPUT_CSV = Path("TESTING_1000bp_18000_per_read_summary.csv")

"""
    Read Kraken report and build a mapping:
       taxid = 'bacteria' / 'virus' / 'other'
    Any taxid listed under 'Bacteria' in the report is labelled 'bacteria',
    any taxid listed under 'Viruses' is labelled 'virus'.
    Everything else is 'other'.
"""

def build_taxid_domain_map(report_path: Path):

    domain_map = {}
    current_domain = None

    with report_path.open() as f:
        # split line into columns, extract taxid and taxon name 
        for line in f:
            parts = line.strip().split()
            if len(parts) < 6:
                continue
            taxid_str = parts[4]
            name = " ".join(parts[5:])
            try:
                taxid = int(taxid_str)
            except ValueError:
                continue

            clean_name = name.strip()

            # Detect top-level domains
            if clean_name == "Bacteria":
                current_domain = "bacteria"
                domain_map[taxid] = "bacteria"
            elif clean_name == "Viruses":
                current_domain = "virus"
                domain_map[taxid] = "virus"
            elif clean_name in ("Archaea", "Eukaryota", "cellular organisms", "unclassified", "root"):
                # leave these as 'other'
                current_domain = None
                domain_map[taxid] = "other"
            else:
                # Inherit domain from parent section, if it is bacteria/virus
                if current_domain in ("bacteria", "virus"):
                    domain_map[taxid] = current_domain
                else:
                    # anything not under bacteria/virus is 'other'
                    domain_map.setdefault(taxid, "other")

    return domain_map


"""
    Map Kraken prediction to 'bacteria' / 'virus' / 'other'.
    - Unclassified (U) or taxid 0 = 'other'
    - If taxid appears under Bacteria in report = 'bacteria'
    - If taxid appears under Viruses in report = 'virus'
    - Otherwise = 'other'
 """

def classify_pred_label(status: str, taxid: int, domain_map):

    if status == "U" or taxid == 0:
        return "other"
    return domain_map.get(taxid, "other")


"""
    get ground truth from read name prefix.
"""

def get_true_label(read_id: str):

    if read_id.startswith("bacteria"):
        return "bacteria"
    elif read_id.startswith("virus"):
        return "virus"
    else:
        return "other"



"""
    Strip the leading 'bacteria_' or 'virus_' part and keep the genome position,
"""

def get_sequence_id(read_id: str):

    parts = read_id.split("_", 1)
    if len(parts) == 2:
        return parts[1]
    return read_id


def main():
    # 1. Build taxid -> domain map from report
    print(f"[INFO] Reading report from {REPORT_PATH} ...")
    domain_map = build_taxid_domain_map(REPORT_PATH)
    print(f"[INFO] Taxids in domain map: {len(domain_map)}")

    # 2. Parse .kraken and write CSV
    print(f"[INFO] Reading kraken file {KRAKEN_PATH} and writing {OUTPUT_CSV} ...")

    with KRAKEN_PATH.open() as infile, OUTPUT_CSV.open("w", newline="") as outfile:
        writer = csv.writer(outfile)
        # Header
        writer.writerow(["status", "true_label", "sequence_id", "taxid", "pred_label"])

        for line in infile:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            # Expect at least: status, read_id, taxid, length...
            if len(parts) < 3:
                continue

            # 'C' or 'U'
            status = parts[0]                
            read_id = parts[1]
            try:
                taxid = int(parts[2])
            except ValueError:
                taxid = 0  
                
            true_label = get_true_label(read_id)
            sequence_id = get_sequence_id(read_id)
            pred_label = classify_pred_label(status, taxid, domain_map)

            writer.writerow([status, true_label, sequence_id, taxid, pred_label])

    print("[INFO] Done! CSV saved as:", OUTPUT_CSV)


if __name__ == "__main__":
    main()
