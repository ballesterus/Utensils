#!/usr/bin/awk -f


BEGIN{RS="\n"; FS=" "}
{ IGNORECASE=1
    if (NF == 2 && $2 ~ /[acgtn-]+$/){
	printf (">"$1"\n"$2"\n")
    }
}
