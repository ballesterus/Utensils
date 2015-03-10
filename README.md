# PoorPhyloTools
Simple scripts for working with sequence data (Fasta) for phylogenetics.

geneStitcher.py		

Concatenates two or aligments in fasta format to produce a supermatrix. It  otputs a log file with the composition of each alignement, its length and the total gaps per file. Additionally produces a Partition file, with the positions of each loci in the supermatrix. This fle is intended to serve as a template for producing program specifica partitioning of datablocks.

The script automatically collects the name of the OTUS from each alignments passed in the argument, and thus their name  should be be the same to be considered the same OTU. The fasta identifies I am using is the following:

>OTU_name|UniqueIdentifier

The script captures the "OTU_name" part of it and discards the idetifier. I'' modify the scrippt to accomodate other fasta identifiers while still capturing the taxon names part of it.


Usage:

python geneSticher.py 1.fasta 2.fasta 3.fasta

or

python geneSticher.py *.fasta