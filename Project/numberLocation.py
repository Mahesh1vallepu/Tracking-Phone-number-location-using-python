# Import necessary libraries

import phonenumbers # For working with phone numbers
import folium # For creating Mpas
from myNumber import number # import phone number from module
from phonenumbers import geocoder, carrier # Function for geolocation and carrier information 

# Set API key
key = "76de1d6e35cb495aba8d9f21946cd610"

# Parse the phone number
PhoneNumber = phonenumbers.parse(number)

# Get geoloctaion and carrier information for the phone number
yourLocation = geocoder.description_for_number(PhoneNumber, "en")
Carrier = carrier.name_for_number(PhoneNumber, "en")

# Print geolocation and carrier information
print(yourLocation)
print(Carrier)

# Import OpenCageGeocode and set up a geocoder
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

# convert location information to string for geocoding
query = str(yourLocation)

# performing geocoding to get detailed location information
result = geocoder.geocode(query)

# Extract lattitude and longitude fro  the information
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

#checking if the phone is valid and possible 
valid = phonenumbers.is_valid_number(PhoneNumber)
possible = phonenumbers.is_possible_number(PhoneNumber)

print(valid,possible)

# Create a map centered at the location with a zoom level of 9
myMap = folium.Map(loaction=[lat,lng], zoom_start=9)

# Add a marker at the location with a popup displaying the location description
folium.Marker([lat,lng],poppup = yourLocation).add_to(myMap)

## save map in html file
myMap.save("myLocation.html")
 
