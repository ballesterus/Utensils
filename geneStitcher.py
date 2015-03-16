#!/Usr/bin/env python
import re
from sys import argv

"""
USAGE: geneStitcher.py alignment1.fasta  alignment2.fasta

This script makes super matrix from a list of fasta files containing aligned sequences. 
It also writes a 'Log' file and a simple partition file, that can then be easily modified to declare partitions or gene blocks fro raxml, or other Phylogeny estimation models.

The script expects the name of the OTU to be the first element in the fasta indetifier, and with a custom character used as a delimiter.

>NAME_of_OTU|Uniqueidentifier   



To accommodate other variants you might need to modify the code or the input seqs.
"""

argv.remove(argv[0])
Delim = raw_input( 'Insert a custom delimiter character separating the OTU name from the sequence indentifier and/or metadata: ')

#print argv #print list of arguments. Activate for debugging.

#Outputfiles
Log = open('StitcherLog.out', 'w+')
Part = open('Partition.txt', 'w+')

#Global variables
OTUS = []

#Classes

class FastaRecord():
    """Class for storing sequence records and related data"""
    def __init__(self, IdLine):
        self.SeqId = IdLine.replace('\n', '').strip('>')
        self.OTU =self.SeqId.split(Delim)[0]
        self.UniqId = self.SeqId.split(Delim)[1]
    

#Function definition
def is_ID(Line):
    """Test whether a string correspond to fasta identifier. herein broadly defined by starting with the '>' symbol"""
    if Line.startswith('>'):
        return True
    else:
        return False

def Get_OTUS(List):
    """ Take a file name  or list ost of file names and populates the global variable with all distinct OTUS found across all input files. The detailed output of this fuction is written to the  Log file """
    for Alignment in List:
        with open(Alignment, 'r') as Al:
            for Line in Al:
                if Line.startswith('>'):
                    Line = Line + Delim
                    OTU = Line.strip('>').split(Delim)[0]
                    if OTU not in OTUS:
                        OTUS.append(OTU)
        
        Log.write("The are are %r OTUS in the input file %s. \n" % (len(OTUS), Alignment))
        [Log.write(OTU + '\n') for OTU in OTUS]
        Al.close()

def Fasta_Parser(File):
    """This function returns a dictionary containing objects of the class FastaRecord, the taxon name or OTU is the index for this Dictionary."""
    with open(File, 'r') as F:
        Records = {}
        Seq=''
        for Line in F:
            if is_ID(Line) and len(Seq) == 0:
                OTU = Line.strip('>').split(Delim)[0]
                Records[OTU] = FastaRecord(Line)
            elif is_ID(Line) and len(Seq) > 0:
                Records[OTU].Seq = Seq
                Records[OTU].SeqLen = len(Seq)
                Records[OTU].SeqGaps = Seq.count('-')
                OTU = Line.strip('>').split(Delim)[0]
                Seq = ''
                Records[OTU]= FastaRecord(Line)
            else:
                Part=Line.replace('\n','')
                Seq = Seq + Part
        Records[OTU].Seq = Seq
        Records[OTU].SeqLen = len(Seq)
        Records[OTU].SeqGaps = Seq.count('-')
    return Records
    F.close()
        
def is_Alignment(Arg):
    """Return True or False after evaluating that the length of all sequences in the input file are the same length. inputs are either file names, or Fasta_record objects."""
    if type(Arg) != dict:
        Arg=Fasta_Parser(Arg)
        Ref = Arg.keys()[0]
        Len= Arg[Ref].SeqLen # obtain a reference from the 1st dict entry.                   
        if all(Len == Arg[key].SeqLen for key in Arg.iterkeys()):
            return True
        else:
            for key in Arg.iterkeys():
                print Arg[key].SeqId
                print Arg[key].SeqLen
            return False
    else:
        Ref = Arg.keys()[0]
        Len= Arg[Ref].SeqLen # obtain a reference from the 1st dict entry.                                           
        if all(Len == Arg[key].SeqLen for key in Arg.iterkeys()):
            return True
        else:
            for key in Arg.iterkeys():
                print Arg[key].SeqId
                print Arg[key].SeqLen
            return False

def Write_Fasta(Dict):
    """Simple Fasta writer. NO wrap No extra features."""
    SuperMatrix = open('SuperMatrix.al', 'w')
    for Record in sorted(Dict.iterkeys()):
        Identifier='>' + Record + '\n'
        Sequence = Dict[Record] + '\n'
        SuperMatrix.write(Identifier)
        SuperMatrix.write(Sequence)
    SuperMatrix.close()

            
# Concatenate Alignments

Get_OTUS(argv) # get a list with all OTUS
SDict={key: '' for key in OTUS} #Makes an Dictionary with all OTUS as keys and and empty sequences.
CL = 0 # Initialize counter for position
for File in argv:
    D=Fasta_Parser(File)
    if is_Alignment(D):
        Role = 0 # Count Otus in Alignment
        Len = D[D.keys()[0]].SeqLen 
        Dummy = '-'* Len #Generates all gap seq for the terminals missing that loci.
        TotalGaps = 0 
        Init = 1 + CL
        End = Init + Len - 1
        CL = End
        Part.write("%s, %d-%d;\n"  % (File.split('.')[0], Init, End))
        for OTU in SDict.iterkeys(): #Populate the Dictionary with Sequences.
            if OTU in D.keys():
                SDict[OTU] = SDict[OTU] + D[OTU].Seq
                Role +=1
                TotalGaps = TotalGaps + D[OTU].SeqGaps
            else:
                SDict[OTU]= SDict[OTU] + Dummy
                TotalGaps = TotalGaps + Len
    else:
        print "Error: The File %d  contains sequences of different lengths!" % File
        break
    Log.write("*" * 70 + '\n')
    Log.write("The alignment of the locus %s file contained %d sequences.\n" % (File, Role))
    Log.write("The length of the alignment is %d positions.\n" % Len)
    Log.write("The alignment contains %d missing entries.\n" % TotalGaps)


Write_Fasta(SDict)
Log.close()
Part.close()
