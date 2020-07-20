#!/bin/awk -f

##############################################################
#         Simple awk script to search fasta records          #
#                                                            #
# Returns the FASTA records whose seq. id. matches a regex   #
# Usage:                                                     #
#     seqlike.awk s=<regex> <file.fasta>                      #
#                                                            #
# Author:J.A. Ballesteros                                    #
# Date:July 2020                                             #
# GPL vers. 3                                                #
##############################################################

BEGIN{
    FS="\n";
    RS=">";
    OFS="";
    m=0;

}

{
    if ($1 ~ s){
	print ">" $0;
	++m 
    }
}
END{
    print "Matches found: ", m
}
