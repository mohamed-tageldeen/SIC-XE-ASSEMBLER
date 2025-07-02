# SIC-XE-ASSEMBLER
# Two-Pass SIC/XE Assembler in Python

This project is a **two-pass assembler for SIC/XE architecture**, implemented in Python. It processes a SIC/XE assembly program and produces corresponding **HTME object code records**. The assembler works in multiple stages, including preprocessing, Pass 1 (location counter and symbol table generation), and Pass 2 (object code generation).

---

## Project Members

[Mohamed Ahmed](https://github.com/mohamed-tageldeen)
[Farah Mahmoud](https://github.com/farah-mahmoudx)


##  Features

- Cleans and tokenizes raw assembly input.
- Performs **Pass 1** to compute location counters and build a symbol table.
- Performs **Pass 2** to generate object code and **HTME records**.
- Outputs intermediate and result files for analysis and debugging.

---

## Assembler Workflow

### Input Preprocessing

- Input: A plain `.txt` file containing the SIC/XE assembly program.
- Strips comments and whitespace.
- Tokenizes instructions into an **intermediate file**.
- Output files:
   - `intermediate.txt` – Tokenized (cleaned) version of the input.

### Pass 1 – Location Counter & Symbol Table

- Computes address (`location counter`) for each instruction.
- Builds a **symbol table** for label-address mapping.
- Output files:
  - `symbol_table.txt` – Label to address mapping.
  - `output_pass1.txt` – Location counter results.

### Pass 2 – Object Code & HTME Record Generation

- Uses intermediate and symbol table files.
- Translates instructions into **object code**.
- Generates:
  - `H` (Header Record)
  - `T` (Text Records)
  - `M` (Modification Records)
  - `E` (End Record)
- Output file:
  - `output_pass2.txt` – Object code line by line.
  - `htme.txt` – Final HTME object code for loading.

---

## How to Run the Assembler

1. Place your input assembly program in a plain text file (e.g., `input.txt`).
2. Ensure that `input.txt` is in the **same directory** as the Python script (`assembler.py`).


