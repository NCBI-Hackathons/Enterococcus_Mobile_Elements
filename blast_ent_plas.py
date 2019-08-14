#!/usr/bin/env

## Generate blastn report for Enterococcuss mobile elements
## author: errol strain, estrain@gmail.com

from argparse import (ArgumentParser, FileType)
import sys
import glob
import subprocess
from decimal import Decimal

def parse_args():
  "Parse the input arguments, use '-h' for help."
  parser = ArgumentParser(description='Generate BLASTN report for Enterococcus Queries')

  # Read inputs
  parser.add_argument('--fasta', type=str, required=True, nargs=1, help='FASTA file')
  parser.add_argument('--db', type=str, required=True, nargs=1, help='Nucleotide BLAST database')
  parser.add_argument('--output', type=str, required=True, nargs=1, help='Output File')
  parser.add_argument('--num_threads', type=int,default=1, nargs=1, help='Number of Threads')
  parser.add_argument('--perc_identity', type=float,default=90, nargs=1, help='Min Percent Identity (0,100)')
  parser.add_argument('--qcov', type=float,default=90, nargs=1, help='Query HSP Coverage (0,100)')
  parser.add_argument('--hsps', type=int,default=1, nargs=1, help='Max Number of HSPS to Report')

  return parser.parse_args()

args =parse_args()

# Gather inputs 
fasta = args.fasta[0]
bdb = args.db[0]

# Get individual and total length of contigs
# cmd = ["awk", "/^>/ {if (seqlen){print seqlen}; ;seqlen=0;next; } { seqlen = seqlen +length($0)}END{print seqlen}",fasta]
# seqlen = subprocess.Popen(cmd,stdout= subprocess.PIPE).communicate()[0]
# intlen = list(map(int,seqlen.splitlines()))
# totlen = sum(intlen)
# Count number of contigs
# numtigs = len(intlen)

# Get coverage information from skesa fasta header
#cmd1 = ["grep",">",fasta]
#cmd2 = ["cut","-f","3","-d","_"]
#p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
#p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE).communicate()[0]
#covdep = map(float,p2.splitlines())
#covlist = [a*b for a,b in zip([float(i) for i in intlen],covdep)]
#covdep = round(sum(covlist)/totlen,1)

# Run blastn
#cmd1 = ["blastn","-db",bdb,"-query",fasta,"-num_threads",str(args.num_threads[0]),"-max_hsps",str(args.hsps),"-subject_besthit","-qcov_hsp_perc",str(args.qcov),"-perc_identity",str(args.perc_identity),"-outfmt","6 qseqid sseqid pident evalue bitscore qlen slen length qstart qend sstart send qcovs"]
cmd1 = ["blastn","-db",bdb,"-query",fasta,"-num_threads",str(args.num_threads[0]),"-subject_besthit","-qcov_hsp_perc",str(args.qcov),"-perc_identity",str(args.perc_identity),"-outfmt","6 qseqid sseqid pident evalue qlen slen length qstart qend sstart send qcovs"]
#cmd1 = ["blastn","-db",bdb,"-query",fasta,"-outfmt","6 qseqid sseqid pident qlen slen length mismatch gapope evalue bitscore qstart qend sstart send","-out","results.tab"]
p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE).communicate()[0]

# write output
output = open(args.output[0],"w")

filehead = str("qseqid\tsseqid\tpident\tevalue\tqlen\tslen\tlength\tqstart\tqend\tsstart\tsend\tqcovs\n")
output.write(filehead)

output.write(p1)

