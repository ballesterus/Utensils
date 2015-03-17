#!usr/bin/env python
import re
import os
from sys import argv

"""A Script for changing names of OTUS in phylogenetic files (or any other text file. In case of fasta files, it replaces the whole identifier line with the new name. for newick, nexux or other file.. it only changes mathcing names.
REplacing names can be easily accoplish using sed, however this scripts is intended to facilitata that task. You can create your reference CSV in any spreadsheet. TODO multiculumn csv  and name editor.

Usage: python  this4that.py names.csv target.fasta
"""

CSV_file = argv[1]
argv.remove(argv[0])
Target = argv
Log = open('this4that.log', 'w')
Map={}



with open(CSV_file, 'r') as F: 
    for Line in F:
        From, To = Line.replace(' ', '').split(',')
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
