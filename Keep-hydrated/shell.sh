time=$1
litres=$(echo "$time * 0.5" | bc)
rounded_litres=$(echo "scale=0; $litres/1" | bc)
echo "time = $1 ---> litres = $rounded_litres"

sleep 5