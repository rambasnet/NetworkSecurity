FROM ubuntu:25.04

ARG DEBIAN_FRONTEND=noninteractive

# Install software packages inside the container
RUN apt update  \
    && apt-get -y install  \
    iputils-ping \
    iproute2  \
    net-tools \
    dnsutils  \
    mtr-tiny  \
    nano      \
    build-essential \
    gdb \
    python3 \
    python3-pip \
    && apt-get clean

WORKDIR /app
# Put file inside the container
COPY hello.py  /app
COPY hello.cpp /app
COPY requirements.txt /app
# Install Python packages
RUN pip install --no-cache-dir --break-system-packages -r /app/requirements.txt 
# Set the environment variable
ENV MY_ENV_VAR=HelloWorld

# The command executed by the container after startup
CMD ["/bin/bash"]
