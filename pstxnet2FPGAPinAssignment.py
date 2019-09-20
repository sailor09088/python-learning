#!/usr/bin/env python3

import re
import sys

net_pattern = re.compile(r'^NET_NAME[\r\n]+$')
net_name_pattern = re.compile(r"^'(.+)'[\r\n]+$")
node_pattern = re.compile(r'^NODE_NAME\s+(\S+)\s+(\S+)[\r\n]+$')

net_list, dev_list = {}, {}
net_name, dev_name = None, None
net, dev = None, None

for line in open(sys.argv[1]):
    m = node_pattern.match(line)
    if m:
        dev_name, pin = m.groups()
        net[dev_name] = pin
        dev = dev_list.get(dev_name, {})
        if not dev:
            dev_list[dev_name] = dev
        dev[net_name] = pin
        continue

    m = net_pattern.match(line)
    if m:
        net_name = None
        net = {}
        continue
    if net is not None and not net_name:
        net_name = net_name_pattern.match(line).group(1)
        net_list[net_name] = net


def list_net():
    for net_name in net_list:
        net = net_list[net_name]
        for dev_name in net:
            pin = net[dev_name]
            print('{net_name} --- {dev_name}.{pin}'.format(**locals()))


def list_dev():
    for dev_name in dev_list:
        dev = dev_list[dev_name]
        for net_name in dev:
            pin = dev[net_name]
            print('{dev_name}.{pin} --- {net_name}'.format(**locals()))
            
            
if len(sys.argv) > 2:
	blacklist = {
	'FLTR_P1_2V_IOFPGA_ATRX',
	'FLTR_P1_2V_IOFPGA_AVCC',
	'FLTR_P1_2V_IOFPGA_PLL0',
	'FLTR_P1_2V_IOFPGA_PLL1',
	'FLTR_P1_2V_IOFPGA_VTTX',
	'VREF_IOFPGA_REF',
	'IOFPGA_CFG_DONE',
	'IOFPGA_CFG_HSWAPEN',
	'IOFPGA_CFG_INIT_L',
	'IOFPGA_CFG_M0',
	'IOFPGA_CFG_M1',
	'IOFPGA_CFG_PROG_L',
	'IOFPGA_CFG_SUSPEND_PD',
	'JTAG_TDO_CPLD',
	'SRT_JTAG_TDO_IOFPGA',
	'JTAG_TMS_MUX',
	'JTAG_TCK_FPGA',
	'P3_3V',
	'P1_2V',
	'P2_5V',
	'P1_8V',	
	'NC',
	'GND'
	}
	dev_name = sys.argv[2]
	dev = dev_list[dev_name]
	for net_name in dev:
		if net_name in blacklist:
			continue
		pin = dev[net_name]
#		print('NET \"{net_name}\" LOC = {pin};'.format(**locals()))
		print('set_location_assignment PIN_{pin} -to {net_name}'.format(**locals()))
#		print('input {net_name},'.format(**locals()))
#		print('{net_name},'.format(**locals()))
else:
	list_dev()
