#!/usr/bin/awk -f 

BEGIN{
    RS=">";
    FS ="\n";
    OFS=""
    ORS=""
    if (ARGC < 3){
	print "usage: awk  [INFILE] [codon number] > outfile";
	exit 1
	}
    c = ARGV[2]
    print c
    delete ARGV[2];
}
{
    if (NF > 1){
	i = c;
	print ">"$1 "\n" 
	sl=length($2);
	while( i <= sl ){
	    print substr($2, i, 1) 
	    i = i + 3;
	}
	print "\n"
    }
}
