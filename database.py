#built by Rishab Budale team Andromeda (Proof of Concept)(beta) 11/12/13 nov 2022
import smtplib
from math import radians, cos, sin, asin, sqrt
nearby_person="$GPGLL,1251.9250,N,07455.4504,E,195048.000,V,N*4C"
target_coords="$GPGLL,1251.9260,N,07455.4504,E,195047.000,V,N*43"

def conversion(nmea):
    var=nmea.split(",")[1].split(".")
    var2=nmea.split(",")[3].split(".")
    print(var)

    print(float(str(var[0][-4])+str(var[0][-3]))+(float(str(var[0][-2])+str(var[0][-1])+"."+var[1])/60))

    longitude=float(str(var[0][-4])+str(var[0][-3]))+(float(str(var[0][-2])+str(var[0][-1])+"."+var[1])/60)
    latitude=float(str(var2[0][-4])+str(var2[0][-3]))+(float(str(var2[0][-2])+str(var2[0][-1])+"."+var2[1])/60)

    return [(longitude),(latitude)]



def send_mail(email,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("username@gmail.com","password")
    server.sendmail("username@gmail.com",email,message)
    server.quit()

def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
     
#----Testing code------------------ 
# driver code
#lat1 = 53.32055555555556
#lat2 = 53.31861111111111
#lon1 = -1.7297222222222221
#lon2 =  -1.6997222222222223


#f=open("//home//rishab//Downloads//Binary2022-11-12_012042.out","r")
#raw=f.read().split("\n")
#print(raw[1])
#------------------------------------

global key
key="username@gmail.com"
selected_keys=[]
target_coordinates=conversion(target_coords)
temp=conversion(nearby_person)
nearby_coordinates=(temp[0],temp[1],key)
nearby_coordinates_list=[nearby_coordinates]
distance_list=[]
max_help=4
max_help_range=3 #in km

def compare_distance():
    for element in nearby_coordinates_list:
        val=distance(element[0], target_coordinates[0], element[1], target_coordinates[1])
        if (val<max_help_range):
            distance_list.append((val,element[2]))
            selected_keys.append(element[2])
            


compare_distance()
for element in selected_keys:
    send_mail(element,"please help at ("+str(target_coordinates[0])+","+str(target_coordinates[1])+") who is "+str(distance_list[0][0])+" km away from you")

print(distance_list)

var=conversion(target_coords)
print(var)