#!/usr/bin/env python3

#Extract net/dev/pin from Concept HDL schematic netlist
#Rev 1.0, 20191009
#Peijun

import re
import sys

#use raw strings by adding an r before the first quote
net_key_pattern = re.compile(r'^NET_NAME[\r\n]+$')
net_name_pattern = re.compile(r"^'(.+)'[\r\n]+$")
node_pattern = re.compile(r'^NODE_NAME\s+(\S+)\s+(\S+)[\r\n]+$')

table = []

for line in open(sys.argv[1]):
	m_node = node_pattern.match(line)
	m_net_name = net_name_pattern.match(line)
	m_net_key = net_key_pattern.match(line)
	if m_net_key:
#		print('1')
		net, dev, pin = None, None, None
#		net_dev_pin = []
	else:
		if m_net_name:
#			print('2')
			net = m_net_name.group(1)
#			print(net)
		else:
			if m_node:
#				print('3')
				dev, pin = m_node.groups()
#				net_dev_pin.append(net)
#				net_dev_pin.append(dev)
#				net_dev_pin.append(pin)
#				print(net_dev_pin)
#				table.append(net_dev_pin)
				print('{net}, {dev}, {pin}'.format(**locals()))
			else:
#				print('4')
				pass
				dev, pin = None, None
#				net_dev_pin = []




