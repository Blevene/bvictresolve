#!/bin/bash
# where $1 is the results and $2 is a list of targets
# $3 is your final results (overlaps)
while read -r p; do
	grep $p $1 | grep -v "127.0.0.1" | sort -n | uniq > $3
done < $2
