#!/usr/bin/awk -f
BEGIN{
	FS=")";
	RS=";";
	OFS="";
	ORS="";
	if (ARGC < 3){
	    print "usage: collapse.awk  [INFILE] [BSvalue] > outfile";
	exit 1
	}
    sup = ARGV[2]
    delete ARGV[2];
}{
    print $1
    for (i=2; i <= NF; i++){
	split($i, B, ",")
	split(B[1], L, ":");
	if (L[1] < sup && L[1] != "" ){
	    sub(L[1]":"L[2], L[1]":0.00", $i);
	    print ")"$i;
	}
	
	else {
	    print ")"$i
	}

    }
    print ";"
}

    




