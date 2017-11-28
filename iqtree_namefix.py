#!/usr/bin/env python

import sys
import os
import re
from sys import argv


def name_catalog(logFile):
    catalog = {}
    switch = 0
    try:
        log= open(logFile, 'r')
    except:
        print "There was a problem reading the file %s" %logFile
        exit(1)
    for line in log:
        if line == "WARNING: Some sequence names are changed as follows:\n":
         # print "Catalog begins"
            switch = 1
            continue
        while switch  == 1:
            if re.search('->', line):
                try:
                    original= re.split('->', line)[0]
                    original =re.sub('[ \n]', '', original)
                    iqname= re.split('->', line)[1]
                    iqname=re.sub('[ \n]', '', iqname)
                    catalog[original]=iqname
                    break
                except:
                    print "ERROR IN: %s" % line
                
            else:
                #print "Done with the catalog"
                #print line
                switch = 0

    log.close()
    return catalog
    
def replaceNames(treefile, catalog):
    with open(treefile, 'r') as infile:
        tree = infile.readline()
        for k in catalog.iterkeys():
            fro = catalog[k]
            to = k
            tree=re.sub(fro, to, tree)
    return tree
    

def main():
    fname= sys.argv[1]
    log = fname.replace('treefile', 'log')
    out = open(fname.replace('fa.treefile', 'tre'), 'w')
    cat = name_catalog(log)
    out.write(replaceNames(fname, cat))
    out.close


               
if __name__ == "__main__":
    if len(argv) == 2:
        main()
    else:
        print "Error: Need the name of iqtree tree file as argument to process."
