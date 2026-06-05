# Complementing a Strand of DNA

## OVERVIEW
This program reads a DNA sequence from a text file, creates **complementary pairs**, and reverses the sequence.
It is a solution to the **"Complementing a Strand of DNA"** Rosalind problem **(ID: REVC)**. The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

---

## FEATURES
- Reads DNA sequence from a file <u>(rosalind_revc.txt)</u>
- Automatically converts input to **uppercase**
- Creates <u>complementary pairs</u> for the DNA
- **Reverses** the DNA sequence
- Fast and memory-efficient — works well with long sequences
- Clean, well-commented code with proper functions and docstrings

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the Input txt with name rosalind_revc.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_revc.txt):
```
AAAACCCGGT
```
**Output:**
```
ACCGGGTTTT
```

---

## HOW IT WORKS
1. The program reads the DNA sequence from the file
2. It cleans the input (removes whitespace and converts to **uppercase**)
3. It changes all letters: <u>A→T, T→A, C→G, G→C</u> and reverses the DNA sequence
4. Finally, it prints the **DNA sequence**

---

## TECHNOLOGIES USED
- **Python**
- **File I/O** (txt)
