#!/usr/bin/python3
from sys import argv
import re


def main1(gff):
    tcatalog={}
    for l in gff:
        l = l.rstrip()
        if not l.startswith('#'):
            fields = l.split('\t')
            if fields[2] in ["mRNA", "snRNA", "rRNA", "snoRNA", "lnc_RNA", "guide_RNA", "transcript", "tRNA", "pseudogene"]:
                if fields[2] == "pseudogene":
                    tranID=re.findall("ID=(.+?);", fields[-1])
                    geneID=tranID
                else:
                    geneID=re.findall("Parent=(.+?);",fields[-1])
                    tranID=re.findall("ID=(.+?);", fields[-1])
                tranfeat="gene_id \"%s\"; transcript_id \"%s\";" %(geneID[0], tranID[0])
                if tranID[0] not in tcatalog.keys():
                    tcatalog[tranID[0]] = tranfeat
    return(tcatalog)



def main2(gff,tcatalog,ogtf):
    gff.seek(0)
    for l in gff:
        l = l.rstrip()
        if not l.startswith('#'):
            fields = l.split('\t')
            if fields[2] in ["CDS", "exon"]:
                attrk=re.findall("Parent=(.+?);",fields[-1])
                del fields[-1]
                fields="\t".join(fields)
                gtfattr=tcatalog[attrk[0]]
                ogtf.write("%s\t%s\n" %(fields, gtfattr)) 
                



def main(ifile):
    igff=open(ifile, 'r')
    ofname =re.sub("gff", "gtf", ifile)
    otf=open(ofname, 'w')
    tcat=main1(igff)
    main2(igff,tcat,otf)
    igff.close()
    otf.close()
    print("CDSs and exon features written into GTF, bye bye!")


if __name__ == "__main__":
    main(argv[1])
