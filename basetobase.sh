#!/bin/bash

input=$1
basei=$2
baseo=$3

until [[ $input != "" ]] && [[ $basei != "" ]]  && [[ $baseo != "" ]]; do
  printf >&2 'This Program Takes 3 Parameters As Input! \nPlease Enter Valid Input! %s\n	ex: ./basetobase.sh [Input] [Base Of Input] [Base Of Output]\n' 
  exit 1
done

#printf '\x$hex'
echo "obase=$baseo;ibase=$basei; $input" | bc
