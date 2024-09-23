#! /bin/bash

sudo apt install -y pandoc texlive texlive-xetex > /dev/null

files=$(find . -name '*.ipynb')
for f in $files; do
    echo Converting: $f
    jupyter nbconvert --log-level=0 --output-dir='./pdfs' --to pdf $f > /dev/null
done
