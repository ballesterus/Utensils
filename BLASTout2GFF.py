#!/usr/bin/env python

from sys import argv

def usage():
    print """Writes a simple genome feature file (GFF) from comma separated BLAST output file (-outfmt 10)\n
    \tUSAGE: BLASTout2GFF.py <BLAST outpu file>

 """

def parse_blastn(fname):
    genes={}
    with open(fname, 'r') as bout:
	for line in bout:
	    [Query,Subject,percid,alnlength,mismatches,gapopenings,qstart,qend,sstart,send,eval,bitscore] = line.split(",")
	    gene=Query
	    if float(eval) < 0.001: 
		try:		
		    if genes[gene][0] == Subject:
			if sstart < genes[gene][2]:
			    genes[gene][2] = sstart
                        elif send > genes[gene][3]:
			    genes[gene][3] =send
			else:
			    if genes[gene][1] > eval:
				genes[gene]=[Subject, eval,sstart,send]
		except:
	            genes[gene]=[Subject,eval, sstart,send]
	return genes
    
def dict_to_gff(DictGenes,ofile):
	O= open(ofile, "w" )
	for k in DictGenes:	
		strand = "+"
		if int (DictGenes[k][2]) > int(DictGenes[k][3]):
			strand= "-"
			O.write("%s\t%s\tuce\t%s\t%s\t%s\t%s\t.\t.\n" %(DictGenes[k][0],k,DictGenes[k][3],DictGenes[k][2],DictGenes[k][1],strand))
		else:
			O.write("%s\t%s\tuce\t%s\t%s\t%s\t%s\t.\t.\n" %(DictGenes[k][0],k,DictGenes[k][2],DictGenes[k][3],DictGenes[k][1],strand))
##MAIN##
if __name__ == "__main__":
    if len(argv) != 2:
        usage()
    else:
        ifile=argv[1]
        oname="%s.gff" % ifile.split(".")[0]
        T=parse_blastn(ifile)
        dict_to_gff(T, oname)
