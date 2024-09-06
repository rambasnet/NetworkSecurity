#! /bin/bash

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
echo "iptables rule added"
echo "list of iptables rules: "
iptables -t nat -L
