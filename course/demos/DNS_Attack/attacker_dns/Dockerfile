FROM handsonsecurity/seed-server:bind

# Copy the configuration and zone files
COPY named.conf  zone_attacker32.com  zone_example.com  /etc/bind/
COPY zone_192.168.0 /etc/bind/

# Start the BIND named service and keep it running
CMD service named start && tail -f /dev/null
