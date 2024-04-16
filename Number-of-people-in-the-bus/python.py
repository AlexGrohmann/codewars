def number(bus_stops):
    psg = 0
    for stop in bus_stops:
        psg = psg + stop[0] - stop[1]
    return psg


def number_fancy(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
