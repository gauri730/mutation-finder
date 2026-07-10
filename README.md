# Mutation Finder: Pairwise Sequence Alignment & Variant Caller

A Python-based comparative genomics tool designed to ingest raw FASTA genomic sequences, perform baseline pairwise alignment, and identify and classify localized nucleotide mutations.

## Project Overview
This tool automates sequence comparison by aligning a sample sequence with a reference sequence. It adapts to differences in sequence length instead of using a direct character-by-character match, allowing reliable identification of structural variations.

The tool maps genomic discrepancies and automatically classifies variants into three core biological mutation profiles:
1. Single Nucleotide Polymorphisms (SNPs): A simple base mismatch substitution where a single character is swapped (e.g., Reference: `A` $\rightarrow$ Sample: `G`).
2. Insertions: New nucleotide bases present in the sample sequence that do not exist in the baseline reference sequence.
3. Deletions: Nucleotide bases present in the baseline reference sequence that are missing from the sample sequence.


## Algorithmic Approach: Pairwise Alignment
To accurately align identical segments and protect matches from frame-shifts caused by indels, the pipeline will use Needleman-Wunsch global alignment
algorithm which is a dynamic programming approach that guarantees an optimal
alignment between two sequences.
The algorithm builds a scoring matrix of size (m+1) x (n+1), where m and n
are the lengths of the reference and sample sequences. Each cell represents
the optimal alignment score up to that point, computed from match/mismatch
and gap scores:

Match Score: +1
Mismatch Penalty: -1
Gap Penalty: -2

Once the matrix is filled, a traceback step walks from the bottom-right
corner back to the origin, therefore reconstructing the optimal aligned sequences
(inserting `-` gap characters where needed).


## Technical Pipeline Architecture

### Stage 1: Data Parsing & Ingestion
Goal: Load and clean the raw FASTA files.
Logic: Read the file line-by-line, skip the header metadata (lines starting with `>`), strip out any hidden newline characters, and join everything into one long, continuous string of DNA characters.
### Stage 2: Sequence Alignment
Goal: Align the cleaned reference sequence against the patient sample sequence.
Logic: Construct a Needleman-Wunsch scoring matrix comparing the reference
and sample sequences, then perform traceback to generate the final aligned
pair of sequences (equal length, gaps inserted where needed).
### Stage 3: Mutation Extraction & Classification
Once the sequences are fully aligned and matched in length including gaps, the script loops through each position ($i$) to check for variants:
If Ref[i] and Sample[i] don't match, and neither is a gap $\rightarrow$ **SNP**
If Ref[i] == '-' but Sample[i] has a base $\rightarrow$ **Insertion**
If Ref[i] has a base but Sample[i] == '-' $\rightarrow$ **Deletion**

### Stage 4: Reporting & Output
Goal: Format and display the discovered mutations.
Logic: Collect the identified variants and log them into a structured layout (like a dictionary or console table) showing the exact position, the mutation type, and the base change (e.g., Position 42: SNP (A -> G)).

## Current Status

- Stage 1 — FASTA parsing and ingestion: **complete**
- Stage 2 — Needleman-Wunsch alignment: **in progress**
- Stage 3 — Variant classification: **in progress**
- Stage 4 — Structured reporting/output: **planned**

This project is under active development. 
