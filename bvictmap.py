#!/bin/env/pyton
# Written by: Blevene
# Make sure you set your default DNS to OpenDNS
# or google, otherwise your ISP will ::mad::
# top-1m.csv is sourced from alexa top 1kk

import csv
import adns
c=adns.init()

reader = csv.reader(open('top-1m.csv', 'r'))
alexadict = {}
for row in reader:
    k, v = row
    alexadict[k] = v

writer = csv.writer(open('plzworkresults.csv', 'wb')) 
resolvdict = {}
count = 0 # Iterator to print to console within for loop
for key, value in alexadict.iteritems():
    try:
        resolved = c.synchronous(value, adns.rr.A)
        resolvdict.setdefault(key, [value]).append(resolved[3])
        for key, value in resolvdict.iteritems():
			writer.writerow([key, value])
	resolvdict = {}
        count += 1
        print "We've resolved %d domains." % count
    except IOError:
        pass
