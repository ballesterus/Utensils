# PoorPhyloTools
Simple scripts for working with sequence data and trees(mostly fasta and newick) for phylogenetics.
<ul>
	<li>geneStitcher.py</li>
	<li>this4that.py</li>
	<li>Dependencies</li>
</ul>

<h3>geneStitcher.py</h3>
Concatenates two or more alignments in fasta format to produce a super-matrix. It outputs a log file that reports on the composition of each alignment, its length and the total gaps per file. Additionally produces a Partition.txt file, with the positions of each loci in the super-matrix. This Partition file is intended to serve as a template for producing program specific partitioning of data-blocks. The script is designed for simple concatenation tasks, more complex operations (chimeras, taxon or site masking, etc.) are not supported. For a more feature rich concatenation platform you can check out SCaFoS (http://megasun.bch.umontreal.ca/Software/scafos/scafos.html).

The script captures the "OTU_name" part of it and discards the unique identifier. It automatically collects the names of the OTUS from each alignment passed in the argument, and thus OTU name part of the identifier should be the same to be considered the same OTU. You will be prompt to provide A delimiter character common in all the input files e. g: "| _  \s , ; :" etc. If your fasta identifiers only have the OTU name (no accession number or other metadata), type any arbitrary character!

It outputs a log file that reports on the composition of each alignment, its length and the total gaps sites per file. Additionally produces a Partition.txt file, with the positions of each input alignment in the supermatrix. This file is intended to serve as a template for producing program specific data-blocks.

The script contains simple functions for parsing and writting fasta (Fasta_Parser(), Write_Fasta()), and class for fasta records (FastaRecord) which can be recycled and repurposed.

Usage:

```>python geneStitcher.py 1.fasta 2.fasta 3.fasta```

or

```>python geneStitcher.py *.fasta```

Example:

File1.fasta:
	 
	 >OTU1|UniqueIdentifier
	 AGATGGATGGAGATTTAGGA
	 >OTU2
	 TTTAGGTATTCTATCAGAGG

File2.fasta:

	>OTU1|ADifferentIndentifier with crazy stuff in the end 13145661.0b:
	TTTGGATTAGTTTAGGA
	>OTU2
	TATTTCAGTAGTTGAGA
	>OTU3|GB|5456464564.4
	CCCCCAATATTATTTTA

```
$./geneSticther File 1.fasta File2.fasta

Insert custom delimiter character, separating the OTU name from the sequence indentifier and/or metadata: |
```
SuperMatrix.al:

	>OTU1	
	AGATGGATGGAGATTTAGGATTTGGATTAGTTTAGGA
	>OTU2
	TTTAGGTATTCTATCAGAGGTATTTCAGTAGTTGAGA
	>OTU3
	--------------------CCCCCAATATTATTTTA

<h3>this4that.py</h3>

Simple leaf renaming script. Automatically renames fasta identifiers, tree leaf nodes, and other ocurrences of the names to replace. Requires a commas delimited file (csv) with exactly two columns; the fisrt column being the current name to match (target), and the second contains the new name (replacement). Does not deletes input files, creates a new version o the input (v2) with the replaced names.

usage: 

```python this4that.csv Names.csv Alignment.fasta DataBlock.nex *bootstrap.tre ```


example csv:
```	
Sp1,Ara_macao
Sp2,Ara_militaris
Sp3,Ara_araurauna
```

TODO:
* Process multiple column csv for flexible renaming.
* For fasta files alert of non modified records.
* Custom name appending and delimiters.
* Get organism name from genebank sequences

<h3>Dependencies</h3>
python 2.7	All scripts are written in pure python and standard modules (os re sys)
