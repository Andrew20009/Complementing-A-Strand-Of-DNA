def read_dna_from_txt(file_path: str) -> str:
    # Reads nucleotide sequence from txt file
    sequence = "" # Initialize empty variable for the sequence
    
    with open(file_path) as f: # Open the file for reading
        for line in f: 
            cleaned = line.strip().upper() # Remove whitespace and convert to uppercase
            sequence += cleaned 
    
    return sequence 


def change_nucleotides(sequence: str) -> str:
    dna = ""  # Initialize empty variable for the DNA
    
    for nucleotide in sequence: # Replace each nucleotide with its complementary base
        if nucleotide == 'A':
            dna += 'T'
        elif nucleotide == 'T':
            dna += 'A'
        elif nucleotide == 'C':
            dna += 'G'
        elif nucleotide == 'G':
            dna += 'C'
        else:
            dna += nucleotide # Protection in case the symbol is not A, T, C, G

    return dna[::-1] # Reverse the complemented strand


if __name__ == "__main__": # Entry point of the code
    file = "rosalind_revc.txt" # Assign the filename to the variable
    seq = read_dna_from_txt(file) 
    dna_final = change_nucleotides(seq)
    
    print(dna_final) # Printing the final result
