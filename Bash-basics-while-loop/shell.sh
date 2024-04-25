#!/bin/bash

x=1
while [ $x -le 20 ]
do
    echo "Count: $x"
    x=$(( $x + 1 ))
done
sleep 5
echo "Count: "{1..20}
sleep 5