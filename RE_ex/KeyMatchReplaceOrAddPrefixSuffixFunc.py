#Rev 0.1
#Python3 exercise code
#Search string with key match
#Add prefix/suffix to string
#Recursive or limited iterations
#Support wildcard symbol
#Print warnings if number of augment is less or more
#Break any line to strings

#!/usr/bin/env python3

import re
import sys

def rpls_func(key, rpls, prefix, suffix, line):
	"""Search then replace or add prefix/suffix"""
	#Search string with key match
	m_str = []
	strs_line = re.split(r'\W+', line)
	for i in range(len(strs_line)):
		if (re.search(key, strs_line[i]) != None):
			m_str.append(strs_line[i])
		else:
			pass
	#Generate string replacement
	for i in range(len(m_str)):
		if (rpls != None):
			line = re.sub(key, rpls, line)
			break
		elif (prefix != None):
			line = re.sub(m_str[i], (prefix + m_str[i]), line)
		elif (suffix != None):
			line = re.sub(m_str[i], (m_str[i]+suffix), line)
	
	return line


key = 'PCIE'
rpls = None
prefix = 'PREFIX_'
suffix = r'_SUFFIX'

file = open(sys.argv[1])
for line in file:
	result = rpls_func(key, rpls, prefix, suffix, line)
	#print
	print(result.upper(), end='')

#End of file