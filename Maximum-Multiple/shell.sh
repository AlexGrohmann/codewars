
divisor=$1
bound=$2

# Initialize the largest integer to 0
largest_N=0

# Loop from 1 up to the bound
for ((i = bound; i > 0; i--)); do
    # Check if the current number is divisible by the divisor
    # and is less than or equal to the bound
    if (( i % divisor == 0 && i <= bound )); then
        # Update the largest integer if the current number meets the conditions
        largest_N=$i
        # Break the loop since we found the largest N
        break
    fi
done

# Output the largest integer N
echo $largest_N

sleep 5