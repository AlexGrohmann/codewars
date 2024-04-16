def number(bus_stops):
    psg = 0
    for stop in bus_stops:
        psg = psg + stop[0] - stop[1]
    return psg
