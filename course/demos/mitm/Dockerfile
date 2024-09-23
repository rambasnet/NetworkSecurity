# Use Kali Linux as base image
FROM kalilinux/kali-rolling:latest

RUN apt update && apt install -y dsniff iptables tcpdump iproute2 python3 python3-pip tmux dnsutils 
RUN apt install -y net-tools iputils-ping

RUN pip3 install scapy mitmproxy
CMD ["/bin/bash"]