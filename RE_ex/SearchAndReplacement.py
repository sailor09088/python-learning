#Rev 0.1
#Python3 exercise code
#Search and replace unicode strings with R.E.
#Recursive or limited iterations
#Support wildcard symbol
#Print warnings if number of augment is less or more
#Break any line to strings

#!/usr/bin/env python3

import re
import sys

#list of pattern followed by substitute
list_pattern_sub_pair = [
	'PMOD1', 'PMOD2',
	'CDM', 'XDM',
	'DMA', 'DMB',
	'DMC', 'DMD'
	]
list_length = len(list_pattern_sub_pair)

#print (list_length)

n=0

file = open(sys.argv[1])
for line in file:
	while n < list_length:
		line = re.sub(list_pattern_sub_pair[n],list_pattern_sub_pair[n+1], line)		
		n = n + 2
	else:
		n = 0
		sys.stdout.write(line.format(**locals()))
		continue
#End of file