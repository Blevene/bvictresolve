#!/bin/bash
# where $1 is the results and $2 is a list of targets
# $3 is the name of a results file, csv for best view
while read -r p; do
	grep $p $1 | grep -v "127.0.0.1" > $3 | sort -n | uniq
done < $2
