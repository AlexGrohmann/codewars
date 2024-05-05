
input_string=$1

length=${#input_string}

output_string=${input_string:1:$((length-2))}
echo "$output_string"

sleep 5

# fancy
arg=$1
echo "${arg:1:-1}"