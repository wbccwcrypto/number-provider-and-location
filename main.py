import phonenumbers
import opencage
import folium


from phonenumbers import geocoder
number = "+918481914956"
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier

service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = "4bc5deeefe2e4f0da38599f37630b409"
geocoder = OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']
print(lat, lng)
myMap=folium.Map(location=[lat, lng], Zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")
