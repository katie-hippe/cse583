#!/bin/bash

# katie
# cse 583
# script to download and unzip pronto data 

rm -rf pronto/
mkdir pronto
cd pronto
touch README.txt
echo "These are 2015 pronto data from a local bike-share system, containing info about rides and users." >> README.txt
mkdir data
cd data
curl -O "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"
unzip open_data_year_one.zip
head *.csv
