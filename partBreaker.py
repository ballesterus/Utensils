#!/usr/bin/env python

 
import argparse
import Get_fasta_from_Ref as GFR 
import re
from sys import argv
import os

def Subsetfromto(FastaDict, outFile, start,end):
    """Writes a subsect multifast file, boud at sequence indeces start and end, form sequence stored in a dictioanry"""
    with open(outFile, 'w') as out:
        for seqID in FastaDict.iterkeys():
            seq=FastaDict[seqID][start:end]
            out.write(">%s\n%s\n" %(seqID,seq))



def main(matrix, partfile, outdir):
    Smatrix=GFR.Fasta_to_Dict(matrix)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    else:
        print 'The output dir already exist!'
    with open(partfile, 'r') as P:
        for pline in P:
            outN=pline.split(',')[0]
            outf="%s/%s" %(outdir,outN)
            start=int(pline.split(',')[1].split('-')[0]) -1
            end=int(pline.split(',')[1].split('-')[1])
            Subsetfromto(Smatrix, outf, start, end)
                    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This is  a simple script for breaking supermatrices in individual MSA based on a partition file. The  required partition file is a two column comma separated value text file where the fisrt column indicates the name of partition, recycled to be used as the name of the output file, and the second column is an interval of the positions in the supermatrix, separated only by "-". This script deals only with consecutive data blocks. Codon partitioning is not implemented... yet.')
 
    parser.add_argument('-in', dest = 'matrix', type = str,   help = 'Input alignemnets in fasta format')
    parser.add_argument('-p', dest = 'partitions', type =str, help = 'Input partiotion definition file: a comma separated text file with two columns, ')
    parser.add_argument('-o', dest = 'outdir', help='Specify directory where to write partitions')
#    parser.add_argument('-c', help="")
    args = parser.parse_args()

    main(args.matrix, args.partitions, args.outdir)
