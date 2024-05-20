import math

# Function to compute coordinates at a given distance and angle
def calculate_coordinates(distance_km, angle_degrees, lat1, lon1):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)

    # Earth's radius in kilometers
    earth_radius_km = 6371.0

    # Convert angle from degrees to radians
    angle_rad = math.radians(angle_degrees)

    # Calculate the change in latitude and longitude
    delta_lat = (distance_km / earth_radius_km) * math.cos(angle_rad)
    delta_lon = (distance_km / earth_radius_km) * math.sin(angle_rad) / math.cos(lat1_rad)

    # Calculate the new latitude and longitude
    lat2_rad = lat1_rad + delta_lat
    lon2_rad = lon1_rad + delta_lon

    # Convert the new latitude and longitude from radians to degrees
    lat2 = math.degrees(lat2_rad)
    lon2 = math.degrees(lon2_rad)

    return lat2, lon2

# Example coordinates and parameters (replace with your own values)
initial_lat = 32.869890  # New York City latitude
initial_lon = 35.091150  # New York City longitude
distance_km = 1.0  # 1 kilometer
angle_degrees = 135.0  # 45 degrees

# new_lat, new_lon = calculate_coordinates(distance_km, angle_degrees, initial_lat, initial_lon)
for angle in [0, 90]:
    print(calculate_coordinates(0.7, angle, initial_lat, initial_lon))
# print(f"Initial Coordinates: Latitude {initial_lat}, Longitude {initial_lon}")
# print(f"New Coordinates: Latitude {new_lat}, Longitude {new_lon}")
