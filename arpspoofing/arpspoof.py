from scapy.all import *

target = int(input())


broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
arp_layer = ARP(pdst=target)
entire_packet = broadcast/arp_layer
answer = srp(entire_packet, timeout=2, varbose=True)[0]