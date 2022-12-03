#built by Rishab Budale team Andromeda (Proof of Concept)(beta) 11/12/13 nov 2022
#navic NMEA data converter to Longitude and Latitude
string="$GPGLL,1251.9260,N,07455.4504,E,195047.000,V,N*43"

var=string.split(",")[1].split(".")
var2=string.split(",")[3].split(".")
print(var)

print(float(str(var[0][-4])+str(var[0][-3]))+(float(str(var[0][-2])+str(var[0][-1])+"."+var[1])/60))

longitude=float(str(var[0][-4])+str(var[0][-3]))+(float(str(var[0][-2])+str(var[0][-1])+"."+var[1])/60)
latitude=float(str(var2[0][-4])+str(var2[0][-3]))+(float(str(var2[0][-2])+str(var2[0][-1])+"."+var2[1])/60)

print(str(longitude)+","+str(latitude))