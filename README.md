FASTA Sequence Extractor

Author: Ashish Jaiswal
Email: ashishfeb13@gmail.com
Description

This script extracts a specified number of FASTA sequences from a multi-FASTA file. It can be used to extract a subset of sequences for further analysis or processing.
Features

    Extracts a specified number of sequences from a multi-FASTA file.
    Logs extraction progress and results to a log file.
    Prints details of the original and extracted files, including the number of sequences.

Usage

    Clone the repository:

    bash

git clone https://github.com/yourusername/fasta-sequence-extractor.git
cd fasta-sequence-extractor

Install dependencies (optional):
There are no external dependencies for this script.

Run the script:

bash

    python extract_sequences.py

    Make sure to replace input.fasta with the path to your input multi-FASTA file.

    Output:
        The extracted sequences will be saved to output.fasta.
        The extraction progress and results will be logged to extraction.log.

Example

To extract the first 10,000 sequences from a multi-FASTA file named input.fasta:

bash

python extract_sequences.py

License

This project is licensed under the MIT License - see the LICENSE file for details.
