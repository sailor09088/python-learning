#!/usr/bin/env python3

#Extract net/dev/pin from schematic netlist
#Rev 1.0, 20191009
#Peijun

import re
import sys

net_pattern = re.compile(r'^NET_NAME[\r\n]+$')
#net_name_pattern = re.compile(r'^\s(\S+)\s[\r\n]+$')
net_name_pattern = re.compile(r"^'(.+)'[\r\n]+$")
node_pattern = re.compile(r'^NODE_NAME\s+(\S+)\s+(\S+)[\r\n]+$')


for line in open(sys.argv[1]):
	m_node = node_pattern.match(line)
	m_net_name = net_name_pattern.match(line)
	m_net = net_pattern.match(line)
	if m_net:
#		print('1')
		net, dev, pin = None, None, None
	else:
		if m_net_name:
#			print('2')
			net = m_net_name.group(1)
			dir(m_net_name)
#			print(net)
		else:
			if m_node:
#				print('3')
				dev, pin = m_node.groups()
				print(net, dev, pin)
			else:
#				print('4')
				dev, pin = None, None




