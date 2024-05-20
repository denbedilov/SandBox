from geopy import distance

start_point = (20, 20)

p1 = distance.distance(meters=5000).destination(start_point, 0)
p2 = distance.distance(meters=5000).destination(start_point, 90)

print(distance.geodesic(p1, start_point).meters)
print(distance.geodesic(p2, start_point).meters)
