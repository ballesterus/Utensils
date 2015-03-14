# PoorPhyloTools
Simple scripts for working with sequence data (Fasta) for phylogenetics.

geneStitcher.py		

Concatenates two or more aligments in fasta format to produce a supermatrix. It outputs a log file that reports on the composition of each alignment, its length and the total gaps per file. Additionally produces a Partition.txt file, with the positions of each loci in the supermatrix. This file is intended to serve as a template for producing program specific partitioning of data-blocks.

The script automatically collects the names of the OTUS from each alignments passed in the argument, and thus names should be the same to be considered the same OTU. The fasta identifier format I am using is the following:

>\>OTU_name|UniqueIdentifier

The script captures the "OTU_name" part of it and discards the unique identifier. I'll modify the script to accommodate other fasta identifier variants while still capturing the taxon names part of it.

Usage:

>python geneStitcher.py 1.fasta 2.fasta 3.fasta

or

>python geneStitcher.py *.fasta

Requires:
python 2.7
