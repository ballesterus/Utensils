 <h1>PhyloUtensils</h1><img src='miLogo.png' width='20%'>

Simple scripts for working with sequence data and trees (mostly fasta and newick) for phylogenetics.s 
<ul>
	<li><a href = '#1'>geneStitcher.py</a></li>
	<li><a href = '#2'>this4that.py</a></li>
	<li><a href = '#3'>RYplace.py<a></li>
	<li><a href = '#4'>splitcodon.awk</a></li>
	<li><a href = '#5'>Dependencies</a></li>
	
	
</ul>

<h3><a name ='1'>geneStitcher.py</a></h3>
Concatenates two or more alignments in fasta format to produce a super-matrix. It outputs a log file that reports on the composition of each alignment, its length and the total gaps per file. Additionally produces a Partition.txt file, with the positions of each loci in the super-matrix. This Partition file is intended to serve as a template for producing program specific partitioning of data-blocks. The script is designed for simple concatenation tasks, more complex operations (chimeras, taxon or site masking, etc.) are not supported. For a more feature rich concatenation platform you can check out SCaFoS (http://megasun.bch.umontreal.ca/Software/scafos/scafos.html).

The script captures the "OTU_name", provided this is the first element in the fasta indentifier (see example below), and discards the rest of the sequence metadata. It first collects the names of the OTU's from each alignment passed in the argument; thus the 'OTU name' part of the identifier should be exactly the same in all files to be considered the same OTU. The Custom delimiter character that separates species (OTU) nam from the sequence id, is provided with the argument -d. 

As outputs, the script produces a ``log'' file that reports on the taxon composition of each alignment, its length and the total gaps sites per file. Additionally produces a Partition.txt file, with the positions of each input alignment in the supermatrix. This file is intended to serve as a template for producing program specific data-blocks.

The script contains simple functions for parsing and writting fasta (Fasta_Parser(), Write_Fasta()), and class for fasta records (FastaRecord) which can be recycled and repurposed.

Usage:

printing help:

```>python geneStitcher.py -h```


```>python geneStitcher.py 1.fasta 2.fasta 3.fasta```

or

```>python geneStitcher.py *.fasta -d '@'```

Example:

File1.fasta:
	 
	 >OTU1@UniqueIdentifier
	 AGATGGATGGAGATTTAGGA
	 >OTU2
	 TTTAGGTATTCTATCAGAGG

File2.fasta:

	>OTU1@ADifferentIndentifier with crazy stuff in the end 13145661.0b:
	TTTGGATTAGTTTAGGA
	>OTU2
	TATTTCAGTAGTTGAGA
	>OTU3@GB|5456464564.4
	CCCCCAATATTATTTTA

```
$./geneSticther File 1.fasta File2.fasta

```
SuperMatrix.al:

	>OTU1	
	AGATGGATGGAGATTTAGGATTTGGATTAGTTTAGGA
	>OTU2
	TTTAGGTATTCTATCAGAGGTATTTCAGTAGTTGAGA
	>OTU3
	--------------------CCCCCAATATTATTTTA

<h3><a name = '2'>this4that.py</a></h3>

Simple leaf (tip, taxon, OTU or terminal node) renaming script. Automatically renames fasta identifiers, tree leaves, and other ocurrences of the names to replace. Requires a commas delimited file (csv) with exactly two columns; the fisrt column being the current name to match (target), and the second contains the new name (replacement). Does not deletes input files, creates a new version o the input (v2) with the replaced names.

usage: 

```python this4that.csv Names.csv Alignment.fasta DataBlock.nex *bootstrap.tre ```


example csv:
```	
Sp1,Araneus_marmoreus
Sp2,Nephila_clavipes
Sp3,Leucauge_venusta
Sp4,Theridiosoma_sp.
```

TODO:
* Process multiple column csv for flexible renaming.
* For fasta files, alert of non modified records.
* Custom name appending and delimiters.
* Get organism name from genebank sequences


<h3><a name='3'>RYplace.py</a></h3>

Recodes nucleotide sequences in the input file(s)(fasta) replacing  purines (A, G) with 'R' and  pyrimidines (T, C) with 'Y'. Its purpose is to ameliorate the effects base composition biases in phylogenetic inference. However, you may want to test first if your data partition sufferes from heterogeneus base composition,  eg. p4 https://code.google.com/p/p4-phylogenetics/

This script takes as argumenets the number of the codon to change 1, 2, 3 or N to recode the whole sequence.
usage:


```python RYplace.py 3 file1.fasta file2.fasta filen.fasta```


The RY coded versions add the suffix '_RY' to the file name.

<h3><a name = '4'>splitcodon.awk</a></h3>

Self explanatory, takes as input a FASTA file and produces a FASTA where only the specified codon positions of the sequences are present. The output is printed to the STDOUT and can be redirected to a file using ">" or ">>".

usage:

```awk splitcodon.awk gene.fasta 3 >  gene_3.fasta```


<h3><a name = '5'>Dependencies<a></h3>
python 2.7	All scripts are written in pure python and standard modules (os re sys).

