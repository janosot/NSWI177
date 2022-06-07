#!/bin/bash
RADIUS=$1
CHAR="X"
EMPTY=" "
for((i=-RADIUS;i<=RADIUS;i++))
do
	STRING=""
	for((j=-RADIUS;j<=RADIUS;j++))
	do
	if (($((i*i)) + ((j*j)) <= $((RADIUS*RADIUS)))); then 
		STRING="$STRING$CHAR"
	else
		STRING="$STRING$EMPTY"
	fi
	done
	echo "$STRING"
done
