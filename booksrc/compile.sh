#! /bin/bash

# disable aslr
read aslr < /proc/sys/kernel/randomize_va_space
if (( $aslr != 0 )); then
    if (( id -u != 0)); then
        echo "Need sudo priviledge to disable aslr..."
    fi
    # provide password for sudo user
    ls /proc/sys/kernel/randomize_va_space
    echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
fi

# compile disabling all the security flags
if (( $# == 1 )); then
    gcc -g -m32 -fno-stack-protector -z execstack -no-pie $1 && echo "Output file is a.out"
elif (( $# == 2 )); then
    gcc -g -m32 -fno-stack-protector -z execstack -no-pie -o $2 $1
else
    echo "Error... No input file provided..."
    echo "./compile.sh <inputfile.c> [a.out]"
fi