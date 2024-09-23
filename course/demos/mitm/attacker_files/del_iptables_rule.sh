#! /bin/bash

iptables -t nat -D PREROUTING 1
iptables -t nat -L
