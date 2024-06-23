#!/bin/bash
nbYear() {
    # Input parameters
    local p0=$1
    local percent=$2
    local aug=$3
    local p=$4
    
    # Convert percent to a fraction
    local growth_rate=$(echo "scale=4; $percent / 100" | bc)
    
    # Initialize variables
    local current_population=$p0
    local years=0
    
    # Loop until the population reaches or exceeds the target population
    while (( current_population < p )); do
        # Calculate new population for the year
        current_population=$(echo "$current_population + ($current_population * $growth_rate) + $aug" | bc)
        current_population=$(echo "$current_population / 1" | bc)  # Round down to the nearest integer
        # Increment the year count
        (( years++ ))
    done
    
    # Output the number of years
    echo $years
}

nbYear $1 $2 $3 $4