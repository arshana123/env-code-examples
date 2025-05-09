def calculate_average(values):
    return sum(values) / len(values)

new_values = [72, 55, 101, 90]
result = calculate_average(new_values)
print(f"Average of {new_values} = {result}")


stations = [
    ['s1', 23],
    ['s2', 97],
    ['s3', 155]
]

def display_stations(stations):
    for station in stations:
        station_id = station[0]
        pm25 = station[1]
        print(f"{station_id} -> {pm25}")

# Test the function
print("Station readings:")
display_stations(stations)


# 1. Function to calculate average PM2.5
def calculate_average(values):
    return sum(values) / len(values)

# Test calculate_average function
new_values = [72, 55, 101, 90]
result = calculate_average(new_values)
print(f"Average of {new_values} = {result}")

# 2. List of stations (tuple format) and display function
stations_list = [
    ['s1', 23],
    ['s2', 97],
    ['s3', 155]
]

def display_stations(stations):
    for station in stations:
        station_id = station[0]
        pm25 = station[1]
        print(f"{station_id} -> {pm25}")

# Test display_stations
print("Station readings:")
display_stations(stations_list)

# 3. Dictionary-style stations and report_status function
def report_status(stations, threshold):
    status_list = []
    for station in stations:
        name = station['name']
        pm25 = station['pm25']
        if pm25 > threshold:
            status = f
