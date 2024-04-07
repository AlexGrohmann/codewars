def coffee_limits(year, month, day):
    CAFE = 51966
    DECAF = 912559
    cafes_allowed = []
    decafs_allowed = []

    # Ensure month and day are formatted as two digits
    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2)

    health_number = int(f"{year}{month_str}{day_str}")

    for i in range(1, 5001):
        cafe_total = health_number + (i * CAFE)
        decaf_total = health_number + (i * DECAF)
        cafe_hex_total = hex(cafe_total)
        decaf_hex_total = hex(decaf_total)

        if "dead" in cafe_hex_total:
            cafes_allowed.append(i)
        if "dead" in decaf_hex_total:
            decafs_allowed.append(i)

    cafes_allowed = cafes_allowed[0] if cafes_allowed else 0
    decafs_allowed = decafs_allowed[0] if decafs_allowed else 0

    return [cafes_allowed, decafs_allowed]
