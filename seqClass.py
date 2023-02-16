#!/usr/bin/env python

# Import packages and functions
import sys, re
from argparse import ArgumentParser

# Create the parser container and specify the arguments sequence and motif
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Exit the program if the number of command line arguments is 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Transform in upper case the sequence, classify the sequence as DNA, RNA, both or neither of the two and print the output
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if 'U' in args.seq and 'T' in args.seq:
        print ('The sequence does not exist')
    elif 'T' in args.seq:
        print ('The sequence is DNA')
    elif 'U' in args.seq:
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Transform in upper case the motif, search for the motif in the sequence and print the output
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("THE MOTIF IS FOUND")
    else:
        print("THE MOTIF IS NOT FOUND")
