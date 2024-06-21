a="$1"
b="$2"
sum=0

# If a and b are equal, return a or b
if [ "$a" -eq "$b" ]; then
    echo "$a"
    exit 1
fi

# Determine the lower and upper bounds
if [ "$a" -lt "$b" ]; then
    lower="$a"
    upper="$b"
else
    lower="$b"
    upper="$a"
fi

# Calculate the sum of integers from lower to upper
for (( i=lower; i<=upper; i++ )); do
    sum=$((sum + i))
done

echo "$sum"