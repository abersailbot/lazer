import gps as gpsd
from point import Point
gps=gpsd.gps(mode=gpsd.WATCH_ENABLE)
previous_lat=0.0
previous_long=0.0
end_p=Point(52.41635 , -4.06660)

while True:
    try:
        if gps.waiting(timeout=2):
            fix = gps.next()
            i = 0
            while fix['class'] != 'TPV':
                if gps.waiting(timeout=2) and i < 15:
                    fix = gps.next()
                    i += 1
                else:
                    print(previous_lat, previous_long)

            previous_lat = fix.lat
            previous_long = fix.lon
            print("here")
            print(fix.lat, fix.lon)
            print(i)
            print("here2")
            p=Point(fix.lat , fix.lon)
            dist=p.distance_to(end_p)
            bear=p.bearing_to(end_p)
            print("DIST = ", dist)
            print("bearing = ", bear)
    except:
        print("there might be no satalites detected")
            

