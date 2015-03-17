#!usr/bin/env python
import re
import os
from sys import argv

"""A Script for changing names of OTUS in phylogenetic files (or any other text file). In case of fasta files, it replaces the whole identifier line with the new name. For newick, nexus or other files.. it only changes matching names.
Replacing names can be easily accomplished using sed, but it might result complicated when renaming hundreds of leaves in many files this script is intended to facilitate that task, with little editing. You can create your reference CSV in any spreadsheet and save it as a comma delited text file.



TODO multiculumn csv  and more complex name editor.

Usage: python this4that.py names.csv target.fasta"""

CSV_file = argv[1]
argv.remove(argv[0])
Target = argv
Log = open('this4that.log', 'w')
Map={}



with open(CSV_file, 'r') as F: 
    for Line in F:
        From, To = Line.replace(', ', '').split(',')
        To = To.strip('\n')
        Map[From] = To

#print Map

for File in Target:
    with open(File, 'r') as F:
        Changes =0
        OutFName = '%s_v2.%s' % (File.split('.')[0], File.split('.')[1])
        Out= open(OutFName,'w')
        for Line in F:
            if Line.startswith('>'):
                Matches =0
                for From in Map.iterkeys():
                    if re.search(From, Line):
                        NL = Map[From]
                        Out.write('>%s\n' % NL)
                        Changes +=1
                        Matches+=1
                if Matches == 0:
                    print 'ALERT: The identifier %s was not found in the names catalog!' % Line

            else:
                for From in Map.iterkeys():
                    if re.search(From, Line):
                        Line = re.sub(From, Map[From], Line)
                        Changes+=1
                Out.write(Line)
        Out.close()
        if Changes == 0:
            os.remove(OutFName)
        else:
            Log.write('%d changes were made in %s' %(Changes, F))
        
Log.close()
