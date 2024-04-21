#!/bin/bash -e
if (($1 % $2 == 0 && $1 % $3 == 0)); then
        echo "true"
    else
        echo "false"
    fi

sleep 5

# different solution to learn more about if statements in bash
n=$1
x=$2
y=$3
a=$((n%x))
b=$((n%y))
if [ "$a" == "0" ] && [ "$b" == "0" ]; then
  echo true
else 
  echo false
fi