"""
Script to extract a specified number of FASTA sequences from a multi-FASTA file.

Author: Ashish Jaiswal
Email: ashishfeb13@gmail.com
"""

import logging

def setup_logging():
    logging.basicConfig(filename='extraction.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def extract_sequences(input_file, output_file, num_sequences):
    """
    Extracts the first num_sequences sequences from the input_file and writes them to the output_file.
    
    Args:
    - input_file (str): Path to the input multi-FASTA file.
    - output_file (str): Path to the output multi-FASTA file.
    - num_sequences (int): Number of sequences to extract.
    """
    logging.info(f"Extracting {num_sequences} sequences from {input_file} to {output_file}...")
    
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        seq_count = 0
        for line in f_in:
            if line.startswith('>'):
                if seq_count >= num_sequences:
                    break
                seq_count += 1
            f_out.write(line)
    
    logging.info(f"Extraction completed. {num_sequences} sequences extracted to {output_file}.")

def print_file_details(file_name):
    """
    Print the number of sequences in a FASTA file.
    
    Args:
    - file_name (str): Path to the FASTA file.
    """
    with open(file_name, 'r') as f:
        num_sequences = sum(1 for line in f if line.startswith('>'))
    
    logging.info(f"Number of sequences in {file_name}: {num_sequences}")

# Input and output file names
input_file = 'input.fasta'
output_file = 'output.fasta'
num_sequences = 10000

# Set up logging
setup_logging()

# Call the function to extract sequences
extract_sequences(input_file, output_file, num_sequences)

# Print details of both files
print_file_details(input_file)
print_file_details(output_file)

# Print completion message
print("Congratulations! You have extracted the number of sequences from the original FASTA file.")

