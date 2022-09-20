#!/usr/bin/env python3

import argparse
from sys import argv
import random

    
def sizegroups(alist):
    d={}
    for i in alist:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    return d

def counte(alist, e):
    n =0
    for x in alist:
        if x == e:
            n+=1
    return n


def list_fastqIDS(areadfile):
    """ This function reads a fastq file and returns a list of the lines that correspond to the fastqId's"""
    result =[]
    linum= 0
    rnum = 0
    wanted =0
    with open(areadfile, 'r') as F:
        for line in F:
           if linum == wanted:
               result.append(rnum)
               linum +=1
               wanted += 4
               rnum +=1
           else:
               linum +=1
            
    return (result)

 

def good_rgroups(nG, listofE):
    """Elemenst are randomly assigned to n groups. Different groups can have different sizes""" 
    possible=list(range(nG))
    gg =[random.choice(possible) for x in listofE]
    return gg


def bad_rgroups(nG, listofE):
    """Elemenst are randomly assigned to n groups of  equal size"""
    gg=[]
    maxsize = int(len(listofE)/nG)
    possible=list(range(nG))
    dc={}
    for i in listofE:
        g = random.choice(possible)
        gg.append(g)
        if g in dc.keys():
            dc[g]+=1
        else:
            dc[g]=1
        if dc[g] == maxsize:
            if len(possible) > 1:
                possible.remove(g)
    return gg

def ugly_rgroups(nG, lissofE):
    """Elements are assigned to equally sized groups according in the order present in the file"""
    gg=[]
    i=0
    g=0
    maxsize = (len(lissofE)/nG)-1
    for a in lissofE:    
        if i < maxsize:
            gg.append(g)
            i+=1
        else:
            i= 0 
            g+=1
            gg.append(g)
    return gg
    

def write_fastq_subsample(alist,sourcefastq):
    oname=sourcefastq.split('.')[0]
    with open(sourcefastq, 'r') as F:
        for i in alist:
            g=i
            outf="%s_sub%d.fastq" %(oname,g)
            with open(outf, 'a+') as out:
                out.write(F.readline())
                out.write(F.readline())
                out.write(F.readline())
                out.write(F.readline())                
        
        

#MAIN
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This script produces good, bad and ugly sub-samples from a source FASTQ-files')
    parser.add_argument('-good', dest= 'good', action ='store_true', default= False, help ='Reads are randomly associated to n groups. Subsamples can have different sizes.')
    parser.add_argument('-bad', dest= 'bad', action ='store_true', default= False, help ='Reads are randomly associated to  n groups resulting in n groups of ~equal size.')
    parser.add_argument('-ugly', dest= 'ugly', action ='store_true', default= False, help ='Reads are associated to n groups of equal size in the order present in the files.')
    parser.add_argument('-n', dest= 'nsubs', type = int, required=True, help ='number of subsamples.')
    parser.add_argument('-i', dest = 'fastqs', type = str, nargs= '+', required = True,  help = 'Input file or files (paired-end reads) in FASTQ format. If pair end reads are provided it is assumed reads occur in the same order in both files')
    args= parser.parse_args()

    #Global variables
    ifiles = args.fastqs
    l =  list_fastqIDS(args.fastqs[0])
    print ("The are %d reads in the source file to be split into %d subsamples" %(len(l), args.nsubs))
    
    if args.bad == True:
        print("Do you really want bad subsamples.... {-_-} alright")
        b = bad_rgroups(args.nsubs, l)
        s = sizegroups(b)
        print ("Here are the number of reads in each subsample:")
        print (s)
        print ("Now to actually write the files. Be patient")
 
        for f in ifiles:
            write_fastq_subsample(b,f)
        print("All done. Please inspect your files M")

    elif args.ugly == True:
        print("Do you really want ugly subsamples.... {^_x} alright")
        u = ugly_rgroups(args.nsubs, l)
        s = sizegroups(u)
        print ("Here are the number of reads in each subsample:")
        print (s)
        print ("Now to actually write the files. Be patient")
 
        for f in ifiles:
            write_fastq_subsample(u,f)
        print("All done. Please inspect your files M")

    elif args.good == True:
        print("Excellent choice! lets get good subsamples.... {^O^} Yay.")
        g = good_rgroups(args.nsubs, l)
        s = sizegroups(g)
        print ("Here are the number of reads in each subsample:")
        print (s)
        print ("Now to actually write the files. Be patient")
 
        for f in ifiles:
            write_fastq_subsample(g,f)
        print("All done. Please inspect your files M")
   
        
