#!/bin/env/python

import csv
import adns
import os.path
c=adns.init()

#Check if results file exists already.
if os.path.isfile('plzworkresults.csv'):
	print "A results file already exists!"
# If no results file, resolve all of the domains in top-1m.csv
else:
	reader = csv.reader(open('top-1m.csv', 'r'))
	alexadict = {}
	for row in reader:
		k, v = row
		alexadict[k] = v
	writer = csv.writer(open('plzworkresults.csv', 'wb')) 
	resolvdict = {}
	count = 0
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
        
