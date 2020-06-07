import ephem
from datetime import *
from time import strftime

#Make an observer
fred      = ephem.Observer()

#PyEphem takes and returns only UTC times. 15:00 is noon in Fredericton
fred.date = datetime.today()

#Location of Fredericton, Canada
#fred.lon  = str(-66.666667) #Note that lon should be in string format
#fred.lat  = str(45.95)      #Note that lat should be in string format#

#Elevation of Fredericton, Canada, in metres
#fred.elev = 20

#To get U.S. Naval Astronomical Almanac values, use these settings
#fred.pressure= 0
#fred.horizon = '-0:34'

#Location of New York, NY
fred.lon = str(-73.9400)
fred.lat = str(40.6700)

#Elevation of New York, NY in meters
fred.elev = 56.6928
fred.pressure=0
fred.horizon= '-0:34'

sunrise=fred.previous_rising(ephem.Sun()) #Sunrise
noon   =fred.next_transit   (ephem.Sun(), start=sunrise) #Solar noon
sunset =fred.next_setting   (ephem.Sun()) #Sunset

#We relocate the horizon to get twilight times
fred.horizon = '-6' #-6=civil twilight, -12=nautical, -18=astronomical
beg_twilight=fred.previous_rising(ephem.Sun(), use_center=True) #Begin civil twilight
end_twilight=fred.next_setting   (ephem.Sun(), use_center=True) #End civil twilight

def convertTZ(x):
	fmt = "%H:%M:%S %Z%z" #define format
	x = ephem.localtime(x) #use pyephem to convert to localtime
	#x = repr(x) 
	return x.strftime(fmt)
	
	
	
	
print "_ twilight   " + convertTZ(beg_twilight) + "_"
print "dawn break " + convertTZ(sunrise)  
print "high noon  " + convertTZ(noon) 
print "dusk sets  " + convertTZ(sunset) 
print "_ twilight   "+convertTZ(end_twilight) + "_"