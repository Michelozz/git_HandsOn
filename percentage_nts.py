#!/usr/bin/env python

# Import packages and functions
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Percentage of each nucleotide in a DNA or RNA sequence')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Transform the input sequence into upper cases. This allows the script to work even if the 
sequence introduced was in lower case (the first step will be to change it to upper case).

args.seq = args.seq.upper()

# From a RNA or DNA sequence, obtain the percentages of each nucleotide
# First we introduce an accumulator set to 0 for each nucleotide. This will add +1 everytime 
it counts the nucleotide specified.
# Then we report whether the sequence is DNA or RNA
# Finally we provide the percentage of each nucleotide
 
nt_contents = { "A":0, "T":0, "C":0, "G":0, "U":0}
if re.search('^[ACGTU]+$', args.seq):
    if 'U' in args.seq and 'T' in args.seq:
        print ('The sequence does not exist')
    else:
        for nt in args.seq: 
            nt_contents[nt] = nt_contents[nt] + 1 
        for key in nt_contents: 
            nt_contents[key] /= len(args.seq) 
            nt_contents[key] *= 100
        for nt, percentage in nt_contents.items():
            print('Percentage of',nt,'in the sequence:', round(percentage))
else:
    print ('The sequence is not DNA nor RNA')
