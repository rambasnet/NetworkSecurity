FROM handsonsecurity/seed-ubuntu:large

RUN apt update && apt install -y dnsutils bind9 \
    && apt clean

# Copy the configuration file for the local DNS server
COPY named.conf           /etc/bind/
COPY named.conf.options   /etc/bind/

# start the DNS server
# keep the container running
CMD service named start && tail -f /dev/null
