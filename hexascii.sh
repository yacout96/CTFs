#!/bin/bash

hex=$1

until [[ $hex != "" ]]; do
  printf >&2 'This Program Takes Some File As Input! \nPlease Enter Valid Input! %s\n' "$filename"
  exit 1
done

#printf '\x$hex'
echo $hex | xxd -r -p
