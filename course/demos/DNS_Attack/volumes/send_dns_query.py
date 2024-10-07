#! /usr/bin/env python3

from scapy.all import *

DNS_SERVER_IP = "8.8.8.8"
# SRC_IP = "10.9.0.1" # tried this, but it didn't work
QUERY_DOMAIN = "www.coloradomesa.edu"


def send_dns_query():
    # Define the target IP address
    IPpkt = IP(dst=DNS_SERVER_IP, src=SRC_IP)
    UDPpkt = UDP(dport=53)
    # Define the DNS query
    DNSpkt = DNS(id=100, qr=0, qdcount=1, qd=DNSQR(qname=QUERY_DOMAIN))
    # Combine the IP, UDP and DNS packets
    request = IPpkt/UDPpkt/DNSpkt
    # Send the request and receive the response
    print("Sending: ", request.show())
    response = sr1(request)
    # Print the response
    print(response.show())


if __name__ == "__main__":
    send_dns_query()
