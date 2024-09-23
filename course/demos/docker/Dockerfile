FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Install software packages inside the container
RUN apt-get update  \
    && apt-get -y install  \
          iputils-ping \
          iproute2  \
          net-tools \
          dnsutils  \
          mtr-tiny  \
          nano      \
    && apt-get clean

# Put file inside the container
COPY Dockerfile  /

# The command executed by the container after startup
CMD ["/bin/bash"]
