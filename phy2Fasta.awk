#!/usr/bin/awk -f

BEGIN{FS= " "; RS="\n"}
{if ($1 !~ /[0-9]/)
    {
	id=$1;
	$1="";
	print ">"id"\n"$0
    }
}
