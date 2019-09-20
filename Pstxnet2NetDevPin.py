#!/usr/bin/env python3

import re
import sys

net_pattern = re.compile(r'^NET_NAME[\r\n]+$')
net_name_pattern = re.compile(r"^'(.+)'[\r\n]+$")
node_pattern = re.compile(r'^NODE_NAME\s+(\S+)\s+(\S+)[\r\n]+$')
end_of_file_pattern = re.compile(r'END.')

net_name	= None
dev_name	= None
pin_name	= None
dev_pin_list	= None

target_dev = sys.argv[2]

blacklist = {
'FLTR_P1_2V_IOFPGA_ATRX',
'FLTR_P1_2V_IOFPGA_AVCC',
'FLTR_P1_2V_IOFPGA_PLL0',
'FLTR_P1_2V_IOFPGA_PLL1',
'FLTR_P1_2V_IOFPGA_VTTX',
}
	
for line in open(sys.argv[1]):	
	netname_match = net_name_pattern.match(line)
	if netname_match:
		net_name = net_name_pattern.match(line).group(1)
		
	node_match = node_pattern.match(line)
	if node_match:
		dev_name = node_pattern.match(line).group(1)
		pin_name = node_pattern.match(line).group(2)
		if net_name in blacklist:
			continue
			if (dev_name == target_dev):
			#print .csv format
				print('{dev_name},{net_name},{pin_name}'.format(**locals()))
