#!/bin/bash

filename=$1
until [[ "$filename" != "" ]]; do
  printf >&2 'This Program Takes A File As Input! \nPlease Enter Valid File! %s\n' "$filename"
  exit 1
done

#read -p "Enter File : " filename

cat $filename | tr 'A-Za-z' 'N-ZA-Mn-za-m'
