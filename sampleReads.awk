#!/usr/bin/awk -f
BEGIN{RS="@";
    ORS="";
    FS="\n"
    if(ARGC< 3){
	n=0;
	count=-1;}
    else{
	n=ARGV[2];
	count=0;}
    delete ARGV[2];
    srand();

    print "Usage:\n\tsampleReads.awk <INFILE.fastq> <NUMBER OF READS TO BE SAMPLED>\n\nIf no number is provided reads will be sampled randomly till the end of the inpuit file.\n\n";

}
{
    OUTF="subsam_" FILENAME;
    OUTF2="unsam_" FILENAME;
    if (rand() >= 0.5 && count < n  && NF > 1){
	print "@" $0 >> OUTF;
	if(n != 0)
	    count=count+1;	
    }	
    else if (NF > 1)
	print "@" $0 >> OUTF2;
	    
}

