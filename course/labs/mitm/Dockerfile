# Use Kali Linux as base image
FROM kalilinux/kali-rolling:latest

RUN apt update && apt install -y iptables tcpdump dsniff iproute2 python3 python3-pip tmux dnsutils 
RUN apt install -y net-tools pipx

RUN pipx install scapy mitmproxy