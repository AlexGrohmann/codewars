odd_or_even() {
    if [ $(( $1 % 4 )) -eq 0 ]; then
        echo "Even"
        elif [ $(( $1 % 4 )) -eq 2 ]; then
        echo "Odd"
    else
        echo "Either"
    fi
}

odd_or_even $1