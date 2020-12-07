#!/bin/sh
while true
do
	clear
	echo '1.ENQ'
	echo '2.ACK'
	read x
	if [ $x -eq 1 ]
	then
		cat enq | socat tcp:127.0.0.1:2577 -
	fi

done
