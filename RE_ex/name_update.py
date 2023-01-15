# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 10:26:06 2023

@author: pqi
"""
import re
import sys

pcie = 'PCIE_TX11_P'
usb = 'USB_SSTX0_N'
kr = '10G_KR_RX3_P'
sata = 'SATA1_RX_N'
mdi = 'GBE0_MDI1_P'
usb2 = 'USB3_N'
old = ''
pattern = re.compile(r'(PCIE_|USB_SS|10G_KR_)(TX|RX)((\d)+)(_P|_N)')
usb_pattern = re.compile(r'(GBE0_MDI|USB)(\d)(_P|_N)')
sata_pattern = re.compile(r'(SATA)(\d)(_)(TX|RX)(_P|_N)')

#for line in open(page48.csa):
for line in open(sys.argv[1]):
    splt = line.split()
    if len(splt) >= 2:
        for i in range (0, len(splt)):
            if splt[i] == 'SIG_NAME':
                old = splt[i+1]
    m = pattern.match(old)
    m2 = usb_pattern.match(old)
    m3 = sata_pattern.match(old)
    if m:
        new = m.group(1)+m.group(2)+m.group(5)+'<'+m.group(3)+'>'
        line = line.replace(old, new)
    if m2:
        new = m2.group(1)+m2.group(3)+'<'+m2.group(2)+'>'
        line = line.replace(old, new)
    if m3:
        new = m3.group(1)+m3.group(3)+m3.group(4)+m3.group(5)+'<'+m3.group(2)+'>'
        line = line.replace(old, new)
    print(line)