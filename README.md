# Network Security and Scapy Notebooks

Jupyter Notebooks for learning network-based exploitations, network utility tools and scapy library - a powerful interactive packet manipulation program for Python.

Some of the contents are based on [Hacking: The Art of Exploitation by Jon Erickson](https://www.amazon.com/Hacking-Art-Exploitation-Jon-Erickson/dp/1593271441/) and [SEED Labs](https://seedsecuritylabs.org/).

Scapy: https://github.com/secdev/scapy/

## Scapy documentation: https://scapy.readthedocs.io/en/latest/


## Requirements

- Ubuntu/Debian Linux (Kali Linux 64-bit Preferred)
  - add account kali:kali with sudo access
- gcc/g++
- Jupyter Notebook
- Python3
- gdb
- peda - python exploit development assistant for gdb
- sqlite3 C/C++ library
- sqlitebrowser
- pwntools
- boost C++ libraries

## Install Required Tools


```bash
sudo apt update
sudo apt upgrade
sudo apt install build-essential
sudo apt install ccache
sudo apt install libboost-all-dev
sudo apt install gcc-multilib g++-multilib
sudo apt install gdb
sudo apt install gdbserver
sudo apt install git
sudo apt install libsqlite3-dev
sudo apt install sqlitebrowswer
pip install ptpython # better python REPL for terminal
```
## Jupyter Notebook

-   Install Python 3.x Miniconda for Linux: https://conda.io/en/latest/miniconda.html
-   Once miniconda is installed, install Jupyter Notebook using conda

```bash
curl -o Miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda.sh # pick defaults; python 3 is installed!
conda update conda
conda install notebook # jupyter notebook
conda install -c conda-forge xeus-cling #c++ kernel
```

## Play with Notebooks

-   Clone/download this repository
-   You must run the notebook as root to use some scappy features such as sniff()
-   Using a terminal cd into the repo folder and run

```bash
sudo jupyter notebook --allow-rot
```
    
-   Open 00-TableOfContents.ipynb chapter and access all the notebooks
