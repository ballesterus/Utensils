#!/usr/bin/env python
import re
import os
from sys import argv

""" RY coding script, Insert as fisrt argument the number 1-3 to replace the corresponding codon or N to recode the whole sequence. Produces an otput file for each file processed with the suffix '_RY'
Usage:

python RYplace.py N *.fasta

"""
Script=argv[0] 
Codon=argv[1]
argv.remove(Script)
argv.remove(Codon)
Targets=argv

##FUNCTION DEFINITIONS


def Is_NT_or_AA(String):
    ''' Returns True  is the sequence is composed of Nucleotide symbols'''
    NT= ('A','C','G','T','U','R','Y','K','M','S','W','B','D','H','V','N')
    AA =('A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','U','V','W','Y','Z','X')
    Comp = set(String)
    if all([i in NT for i in Comp]):
        return True
    elif all([i in AA for i in Comp]):
        return False
#        print 'This seems to be a AA sequenece.'
    else:
        return False
#       print  'Not valid sequence'
    


def All_2_RY(Sequence):
    NL = ''
    Index = 1
    for base in Sequence:
        Index += 1
        if base == 'A' or base == 'G':
            NL += 'R'
        elif base =='T' or base =='C':
            NL += 'Y'
        else:
            NL += base
    return NL

def Codon_2_RY(Sequence, Position):
    Pos = int(Position)
    Index = 1 + (3 - Pos)
    NL = ''
    for base in Sequence:
        if (Index + 3) % 3 == 0:
            if base == 'A' or base == 'G':
                NL += 'R'
            elif base =='T' or base =='C':
                NL += 'Y'
            else:
                NL += base
        else:
            NL += base
        Index += 1
    return  NL

## REPLACING

if Codon not in ['1','2','3', 'N']:
    print "ERROR: USE numbers 1 to 3 to specify the codon to recode or 'N' to recode the whole sequence."

for File in Targets:
    with open(File, 'r') as F:
        OutFName = '%s_RY.%s' % (File.split('.')[0], File.split('.')[1])
        Out= open(OutFName,'w')
        for Line in F:
            Line = Line.strip('\n')
            if Line.startswith('>'):
                Out.write(Line + '\n')
            else:
                if Is_NT_or_AA(Line):
                    if Codon == 'N':
                        Out.write(All_2_RY(Line) + '\n')
                    else:
                        Out.write(Codon_2_RY(Line, Codon) + '\n')

