#!/bin/bash

input=$1
Orange=$'\033[1;93m'
NoColor=$'\033[0m'
until [[ $input != "" ]]; do
  printf >&2 'This Program Takes Some File As Input! \nPlease Enter Valid Input! %s\n' "$filename"
  exit 1
done

#HEX Base 16
echo -e "${NoColor}From Hex To ASCII : $Orange" 
echo $input | xxd -r -p 
echo -e "\n"
#OCT Base 8
#BIN Base 2
#DEC Base 10

