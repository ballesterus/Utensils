#!/usr/bin/env python
import re
import os
#import UPhO
from sys import argv


"""A Script for changing names of OTUS in phylogenetic files (or any other text file). In case of fasta files, it replaces the whole identifier line with the new name. For newick, nexus or other files it only changes matching names.
Replacing names can be easily accomplished using sed or regex, but it might result complicated when renaming hundreds of leaves in many files this script is intended to facilitate that task, with little editing. You can create your reference CSV in any spreadsheet and save it as a comma delimited text file.

This script does not replace the input file, instead creates a version of the same file with 'v2' in its name. 


TODO 
    * multiculumn csv and more complex name editor.
    * verify all identifiers where replaced or write an alert.
Usage: 
    python this4that.py names.csv target.fasta
    or
    python this4that.py names.csv *.faa
    """



CSV_file = argv[1]
argv.remove(argv[0])
argv.remove(CSV_file)
#print argv
Target = argv
Log = open('this4that.log', 'w')

def makefromtodict(namesCSV):
    namesdict={}
    with open(namesCSV, 'r') as F: 
        for Line in F:
            try:
                From, To = Line.replace(', ', '').split(',')
                To = To.strip('\n')
                namesdict[From] = To
            except:
                print "ERROR on: %s" % (Line)
    return namesdict


###MAIN###


FTdict=makefromtodict(CSV_file)
for File in Target:
    with open(File, 'r') as F:
        Changes =0
        OutFName = '%s_renamed.%s' % (File.split('.')[0], File.split('.')[1])
        Out= open(OutFName,'w')
        for Line in F:
            for From in FTdict.iterkeys():
                 To=FTdict[From]
                 reexpress="(?<![0-9A-Za-z_:|\.])%s(?=[,;\):\n\s])" % From
                 if re.search(reexpress, Line):
                     Line=re.sub(reexpress, To, Line)
                     Changes +=1
            Out.write(Line)
        Out.close()
        print "Names found/changed in %s = %d\n" %(File,Changes)
        if Changes == 0: 
            Log.write('%s: %d changes.' %(File, Changes))
            os.remove(OutFName)
        else:
            Log.write('%s: %d changes.' %(File, Changes))
        
        Log.close()
print "All done!"
