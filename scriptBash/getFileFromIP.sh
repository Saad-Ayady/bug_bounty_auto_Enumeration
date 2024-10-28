#!/bin/bash
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
RESET='\e[0m'
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <file IP's> <word list For files>"
    exit 1
fi
file=$1
worl=$2

while IFS= read -r line; do
  ip_to_scan=$(echo "$line" | awk -F'.' '{print $1"."$2}')
  for i in {0..255}; do
    for j in {0..255}; do
      ipa="${ip_to_scan}.${i}.${j}"
      while IFS= read -r ff; do
        wget -t 1 -T 2 "http://${ipa}/${ff}"
      done < "$worl"
    done
  done
done < "$file"
