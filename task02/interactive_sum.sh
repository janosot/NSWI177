#!/bin/bash
sum=0
   echo "= "$sum
   printf "+ "
while read -r num
do
   sum=$(( sum + num ))
   echo "= "$sum
   printf "+ "
done
