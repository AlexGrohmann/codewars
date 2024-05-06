#!/bin/bash
START=1
END=$1
string=$2
result=""

# Now loop it
for ((i=$START; i<=$END; i++))
do
    result+="$string"
done

echo "$result"

sleep 5