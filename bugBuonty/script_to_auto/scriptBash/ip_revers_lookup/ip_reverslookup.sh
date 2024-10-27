#!/bin/bash
RED='\e[31m'
YELLOW='\e[33m'
RESET='\e[0m'
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 < file IP's > < name of output file >"
    exit 1
fi
file=$1
outputName=$2
while IFS= read -r line; do
    pages=$(curl -s "https://rapiddns.io/sameip/${line}?page=1" | grep '<a class="page-link"' | grep -o 'page=[0-9]*">' | awk -F'=' '{print $2}' | sed 's/">//' | sort -n | tail -n 1)
    echo -e "[!]${RED}Pages in This Ip ${line} : ${pages} ${RESET}"
    for (( i=1; i <= $pages; i++ )); do
      echo -e "${YELLOW}[+] Req to page namper ${i} ${RESET}"
      com=$(curl -s "https://rapiddns.io/sameip/${line}?page=${i}" | grep "<td>" | grep "</td>" | grep "[A-za-z0-9_].[A-za-z]"| grep -v "<td>A</td>" | sed 's/<td>//g' | sed 's/<\/td>//g' )
      if [ -z "$com" ]; then
        $i=$pages + 1
      else
        curl -s "https://rapiddns.io/sameip/${line}?page=${i}" | grep "<td>" | awk -F'<td>' '{print $2}' | grep "[A-za-z0-9_].[A-za-z]" | grep -v "<a" | sed 's/<\/td>//g' | tee -a $outputName
      fi
    done
  # fi
done < "$file"
