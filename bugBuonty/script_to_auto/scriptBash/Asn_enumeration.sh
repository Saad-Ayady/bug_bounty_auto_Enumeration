#!/bin/bash
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
RESET='\e[0m'
if [ -z "$1" ]; then
    echo -e "${RED}Usage: $0 <target>${RESET}"
    exit 1
fi
target=$1
output_file="${target}_asn.txt"

echo -e "[${GREEN}*${RESET}] ${YELLOW} STARTING Get ASN for ${RED} ${target} ${RESET}"
curl -s https://api.bgpview.io/search?query_term=$target | jq | grep '"asn":' | awk '{print $2}' | sed 's/,//g' > "$output_file"
if [[ ! -f "$output_file" ]]; then
    echo "Error in Saving file :("
    exit 1
fi

while IFS= read -r line; do
    nmap --script targets-asn --script-args targets-asn.asn=$line >> "nmap_${output_file}" 2>/dev/null
done < "$output_file"

cat "nmap_${output_file}" | grep "/[0-9]" | awk '{print $2}' > "ASN_outPut_${target}.txt"
rm $output_file
rm "nmap_${output_file}"
echo -e "[${GREEN}+${RESET}] ${YELLOW} SAVE ALL IP's IN ${RED} ASN_outPut_${target}.txt"
