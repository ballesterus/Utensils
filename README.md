# PoorPhyloTools
Simple scripts for working with sequence data (Fasta) for phylogenetics.

###*geneStitcher.py
Concatenates two or more alignments in fasta format to produce a super-matrix. It outputs a log file that reports on the composition of each alignment, its length and the total gaps per file. Additionally produces a Partition.txt file, with the positions of each loci in the super-matrix. This Partition file is intended to serve as a template for producing program specific partitioning of data-blocks. The script is designed for simple concatenation tasks, more complex operations (chimeras, taxon or site masking, etc.) are not supported. For a more feature rich concatenation platform you can check out SCaFoS (http://megasun.bch.umontreal.ca/Software/scafos/scafos.html).

The script captures the "OTU_name" part of it and discards the unique identifier. It automatically collects the names of the OTUS from each alignment passed in the argument, and thus OTU name part of the identifier should be the same to be considered the same OTU. You will be prompt to provide A delimiter character common in all the input files e. g: | _ \ \s , ; : etc. If your fasta identifiers only have the OTU name (no accession number or other metadata), type any arbitrary character, so the script unpacks the name of the OTU  correctly!

Concatenates two or more aligments in fasta format to produce a supermatrix. It outputs a log file that reports on the composition of each alignment, its length and the total gaps per file. Additionally produces a Partition.txt file, with the positions of each loci in the supermatrix. This file is intended to serve as a template for producing program specific partitioning of data-blocks.


Usage:

>python geneStitcher.py 1.fasta 2.fasta 3.fasta

or

>python geneStitcher.py *.fasta


Example:

File1.fasta:
	 
	 >OTU1|UniqueIdentifier
	 AGATGGATGGAGATTTAGGA
	 >OTU2
	 TTTAGGTATTCTATCAGAGG


File2.fasta:

	>OTU1|ADifferentIndetifier with crazy stuff in the end 13145661.0b:
	TTTGGATTAGTTTAGGA
	>OTU2
	TATTTCAGTAGTTGAGA
	>OTU3|GB|5456464564.4
	CCCCCAATATTATTTTA


>./geneSticther File 1.fasta File2.fasta

	Insert custom delimiter character, separating the OTU name from the sequence indentifier and/or metadata: |


SuperMatrix.al:

      >OTU1	
      AGATGGATGGAGATTTAGGATTTGGATTAGTTTAGGA
      >OTU2
      TTTAGGTATTCTATCAGAGGTATTTCAGTAGTTGAGA
      ¯>OTU3
      --------------------CCCCCAATATTATTTTA



Requires:
python 2.7
