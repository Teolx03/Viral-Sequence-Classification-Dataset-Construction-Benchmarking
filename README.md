# Viral Sequence Classification: Dataset Construction & Benchmarking

**A Python-based bioinformatics project focusing on large-scale genomic data processing, dataset construction, and classification model benchmarking.**

## Project Overview

This university group project investigated computational approaches for distinguishing viral and bacterial DNA sequences.

The team developed two composition-based classification models:

- **KLM (K-mer-GC-Logistic Regression Model):** Combines k-mer log-odds scores and GC content using logistic regression.
- **KMM (K-mer-Markov-corrected Model):** Uses Markov-corrected k-mer scores for viral sequence classification.

The models were evaluated alongside Kraken2 and VirFinder to compare classification accuracy and computational efficiency.

My primary contributions focused on **genomic dataset construction, Python-based data processing, and benchmarking Kraken2 and KMM**.

**Project Type:** University Group Project

**Programming Language:** Python

**Tools & Technologies:** Biopython, NCBI Entrez API, Pandas, Linux, Kraken2

**Key Skills:** Data Retrieval, Random Sampling, Data Preprocessing, Dataset Construction, Data Validation, Model Benchmarking, Performance Evaluation

---

## My Contributions

### 1. Genomic Data Retrieval & Random Sampling

- Obtained bacterial genome accession ID lists from NCBI.
- Used Python's `random.sample()` to randomly select accession IDs from downloaded lists.
- Retrieved corresponding genomic sequences using Biopython's `Entrez.efetch()` API.
- Organized downloaded sequences into FASTA files for subsequent processing.

**Relevant Script:** [download_bacteria(1).py](./dataset_preparation/download_bacteria%281%29.py)

### 2. Large-Scale Dataset Construction

- Processed viral and bacterial genomes into fixed-length DNA fragments using Python and Biopython.
- Applied bacterial phylum-based sampling during dataset construction to improve representation.
- Constructed a balanced training dataset containing **418,210 DNA fragments**, comprising 209,105 viral and 209,105 bacterial fragments.
- Prepared separate datasets for model development and evaluation.
- Generated five testing datasets with fragment lengths ranging from 1,000 bp to 5,000 bp.

Each final testing dataset contained 18,000 sequences, including 9,000 viral and 9,000 bacterial fragments, enabling consistent benchmarking across fragment lengths.

### 3. FASTA Data Processing & Validation

Developed Python scripts to support different stages of dataset preparation:

- **FASTA Window Splitting:** Divided genomic sequences into fixed-length, non-overlapping fragments.
- **FASTA File Combination:** Combined multiple FASTA files and counted the resulting sequences.
- **Sequence Validation:** Compared nucleotide sequences between FASTA files to identify mismatches and verify consistency.

### 4. Kraken2 Execution & Model Benchmarking

- Executed Kraken2 on a Linux-based university server.
- Processed Kraken2 classification reports and per-sequence outputs using Python.
- Mapped taxonomic predictions into bacterial, viral, and other categories.
- Compared predicted classifications against known sequence labels.
- Calculated classification performance metrics, including accuracy, precision, sensitivity, specificity, and F1 score.
- Benchmarked Kraken2 and KMM across datasets with different DNA fragment lengths.

---

## Project Workflow

The overall workflow covered the following stages:

**Stage 1 — Data Retrieval**

NCBI accession ID lists → Random selection → Genome retrieval through Biopython

**Stage 2 — Dataset Preparation**

FASTA sequences → Fixed-length fragmentation → Dataset combination and sequence validation

**Stage 3 — Classification**

Prepared testing datasets → Kraken2 classification on Linux server

**Stage 4 — Performance Evaluation**

Kraken2 outputs → Classification result processing → Confusion matrix and performance metrics

The repository contains scripts supporting these stages, rather than a fully automated end-to-end pipeline.

---

## Python Scripts

### Dataset Preparation

| Script | Description |
|---|---|
| [download_bacteria(1).py](./dataset_preparation/download_bacteria%281%29.py) | Randomly selects bacterial accession IDs from a local list and retrieves sequences through NCBI Entrez |
| [fasta_window_split.py](./dataset_preparation/fasta_window_split.py) | Splits FASTA sequences into fixed-length DNA fragments using Biopython |
| [fasta_combine.py](./dataset_preparation/fasta_combine.py) | Combines multiple FASTA files and counts the total number of sequences |
| [compare_sequence.py](./dataset_preparation/compare_sequence.py) | Compares nucleotide sequences from FASTA files and identifies mismatches |

### Kraken2 Benchmarking

| Script | Description |
|---|---|
| [run_kraken.py](./kraken2_benchmarking/run_kraken.py) | Executes Kraken2 classification and records execution time |
| [analysis_Kraken_result.py](./kraken2_benchmarking/analysis_Kraken_result.py) | Processes Kraken2 reports and outputs a CSV containing true and predicted labels |
| [benchmark_statistic.py](./kraken2_benchmarking/benchmark_statistic.py) | Calculates confusion matrix values and classification performance metrics |

---

## Benchmark Results

The overall group project compared four classification models on a common testing dataset containing **18,000 DNA fragments of 1,000 bp each**.

| Model | Accuracy | Precision | Sensitivity | Specificity | AUC-ROC | Runtime |
|---|---|---|---|---|---|---|
| KLM | 86.76% | 84.69% | 89.74% | 83.78% | 0.9515 | 58.44 s |
| KMM | 84.51% | 80.10% | 91.83% | 77.19% | 0.9389 | 103.69 s |
| VirFinder | 80.09% | 85.44% | 72.54% | 87.63% | 0.8665 | 334.70 s |
| Kraken2 | 97.00% | 99.70% | 94.40% | 99.70% | N/A | 8.22 s |

### Key Findings

- **Kraken2** achieved the highest accuracy (97.00%) and shortest runtime (8.22 seconds) under the reported benchmarking conditions.
- **KLM** achieved higher classification accuracy than KMM and VirFinder.
- **KMM** showed relatively high sensitivity but lower specificity, highlighting a trade-off between viral detection and false-positive classification.
- Across testing datasets with fragment lengths increasing from 1,000 bp to 5,000 bp, KMM accuracy increased from 84.51% to 87.14%, with a corresponding increase in runtime.

These results are based on the group's reported experiments and are specific to the testing datasets and computational environment used.

---

## Project Report

[Report](./Report.pdf)

The individual reflective report documents the dataset construction methodology, benchmarking procedures, project results, personal contributions, and reflections.

---

## Requirements

- Python 3
- Biopython
- Pandas and NumPy
- Kraken2 (for classification execution)
- NCBI Entrez access (for sequence downloading)

Install the required Python packages:

```bash
pip install biopython pandas numpy
```

**Execution Notes:**

- The Python scripts use predefined input and output filenames based on the original project environment.
- The NCBI retrieval script requires a valid email address and an input accession ID list.
- Kraken2 execution requires an installed Kraken2 environment, a compatible reference database, and input FASTA files.
- The filenames used across scripts may require adjustment before running them together.
- The complete classification model implementations and large genomic datasets are not provided in this repository.

---

## Data Availability

The original genomic datasets and accession ID lists are not included due to dataset size and unconfirmed redistribution permissions.

This repository provides selected Python scripts used in the data preparation and Kraken2 benchmarking workflow.

The scripts demonstrate individual processing and evaluation tasks but do not independently reproduce the complete model development and benchmarking experiments without the original data, computational environment, and additional project components.

---

## Project Context

This project was completed collaboratively as part of the **Biomedical Informatics** coursework at Zhejiang University–University of Edinburgh Institute.

My individual responsibilities primarily involved large-scale genomic data retrieval, dataset preparation, sequence processing, and performance benchmarking using Python, Biopython, Linux, and Kraken2.

Through this project, I gained practical experience in managing large biological datasets, developing Python-based processing scripts, validating data quality, and evaluating computational models using quantitative performance metrics.
