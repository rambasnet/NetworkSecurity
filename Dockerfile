FROM handsonsecurity/seed-ubuntu:large

RUN apt update \
  && apt install -y \
  g++ gcc make sqlite3 time curl git nano dos2unix \
  net-tools iputils-ping iproute2 sudo gdb less \
  && apt clean;

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
