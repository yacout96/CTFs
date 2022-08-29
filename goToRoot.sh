#!/bin/bash

echo -e "\nPlease execute with source (ex. 'source goToRoot.sh') \n\n"

while :
do
	if [[ $(find * -maxdepth 0 -type d) ]] ; then
		a=$(ls -d */)
		echo "Changing Directory To : $a"
		cd */.
	else 
		echo -e "\n\nReached The End , Files In The Directory Are : "
		ls
		break
	fi
done

