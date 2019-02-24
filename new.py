from firebase import firebase
import gmplot
import gmaps
import time
import urllib
import urllib2
import webbrowser
from selenium import webdriver
from math import sin, cos, sqrt, atan2, radians

R = 6373.0

firebase = firebase.FirebaseApplication('https://hackcu-36162.firebaseio.com')

lattitude_array = []
longitude_array = []

count = 1
Total_distance = 0
distance = 0

while True:

	result = firebase.get('https://hackcu-36162.firebaseio.com', None)

	size = int(result['Array_Size'])

	lat_val = "Latitude_%d" %count

	long_val = "Longitude_%d" %count

	if(count > size):
		break

	print(result[lat_val])

	print(result[long_val])

	gmap1 = gmplot.GoogleMapPlotter(float(result[lat_val]), float(result[long_val]), 26, "AIzaSyBVNhX8PR3EKWrBnXDbrFiHmrj9qyqVzRU")

	lattitude_array.append(float(result[lat_val]))

	longitude_array.append(float(result[long_val]))

	if(count > 1):
		lat1 = radians(lattitude_array[count - 2])
		lat2 = radians(lattitude_array[count - 1])
		lon1 = radians(longitude_array[count - 2])
		lon2 = radians(longitude_array[count - 1])

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c

		#distance = sqrt((dlon ** 2) + (dlat ** 2))

	Total_distance = Total_distance + distance

	count = count + 1

for i in range(size):
	gmap1.marker(lattitude_array[i], longitude_array[i], 'cornflowerblue')

print(Total_distance)
#gmap1.plot(40.0102, -105.2424, 'cornflowerblue', edge_width=10)

#gmap1.scatter(40.0102, -105.2424, '#FF0000', size=30, marker = True)

#markers = gmaps.marker_layer(40.0102, -105.2424)

gmap1.draw("map11.html")

webbrowser.open("map11.html", new = 0)
