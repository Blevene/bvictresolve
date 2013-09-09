#!/bin/bash
# where $1 is the results and $2 is a list of targets
# redirect the results to a file of your choice
while read -r p; do
	cat $1 | grep $p | grep -v "127.0.0.1" | sort -n | uniq
done < $2
