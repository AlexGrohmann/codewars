#!/bin/bash

# Function to convert month name to number
get_month_number() {
    case "$1" in
        "jan" | "january") echo "01";;
        "feb" | "february") echo "02";;
        "mar" | "march") echo "03";;
        "apr" | "april") echo "04";;
        "may") echo "05";;
        "jun" | "june") echo "06";;
        "jul" | "july") echo "07";;
        "aug" | "august") echo "08";;
        "sep" | "sept" | "september") echo "09";;
        "oct" | "october") echo "10";;
        "nov" | "november") echo "11";;
        "dec" | "december") echo "12";;
        *) echo "Invalid month";;
    esac
}

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <month>"
    exit 1
fi

# Convert month name to lowercase before processing
month=$(echo "$1" | tr '[:upper:]' '[:lower:]')

# Get the number of the month
month_number=$(get_month_number "$month")

# Print the result
echo "$month_number"


sleep 5