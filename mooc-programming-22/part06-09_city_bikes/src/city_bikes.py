def get_station_data(filename: str):
    station_dictionary = {}

    with open(filename) as station_file:
        for line in station_file:
            line = line.replace("\n", "")
            data = line.split(";")
            
            if data[0]=="Longitude":
                continue

            station_dictionary[data[3]] = (float(data[0]), float(data[1]))

    return station_dictionary

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    import math

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    station_one = ""
    station_two = ""
    max_distance = 0

    for first_station in stations:
        for second_station in stations:
            if distance(stations, first_station, second_station) >= max_distance:
                max_distance = distance(stations, first_station, second_station)
                station_one = first_station
                station_two = second_station

    return station_one, station_two, max_distance

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')

    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)

    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)