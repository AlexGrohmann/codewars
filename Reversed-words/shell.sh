input_string="$1"
# Split the string into an array of words
IFS=' ' read -r -a words_array <<< "$input_string"
# Reverse the array and print the words
for (( i=${#words_array[@]}-1; i>=0; i-- )); do
    if [ $i -eq 0 ]; then
        echo -n "${words_array[$i]}"
    else
        echo -n "${words_array[$i]} "
    fi
done
echo

sleep 5