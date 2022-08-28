#!/bin/bash

ascii=$1

until [[ $ascii != "" ]]; do
  printf >&2 'This Program Takes Some File As Input! \nPlease Enter Valid Input! %s\n' "$filename"
  exit 1
done

cat $ascii | awk '{ printf("%c",$0); }'
