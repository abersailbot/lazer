def gps_loc(): # if having consistancy problems run gpsd in background
    import gps
    session=gps.gps(mode=gps.WATCH_ENABLE)
    lat=""
    lon=""
    for i in range(1,10): # currently running at 10 times to ensue data is collected
        report=session.next()
        report2=str(report)
        print(report2[10])
        print(report)
        lat_start=0
        lat_end=0
        lat=""
        lon_start=0
        lon_end=0
        lon="" #above is all initiation
        try:
            lat_start=report2.index("'lat': ") # report2 outputs as a long data string the try and expect finds the start and end of usefull data in the string
            print("found")
            lat_end=report2.find(",",lat_start)
            print(lat_start,"to",lat_end)
        except:
            print("not found")
        for i in range((lat_start+7),lat_end):
            temp=report2[i]
            
            lat=lat+temp # adds individual numbers to string via concatination
            
        try: # here starts the repeat of the above but for lon (longitude)
            lon_start=report2.index("'lon': ")
            print("found")
            lon_end=report2.find(",",lon_start)
            print(lon_start,"to",lon_end)
        except:
            print("not found")
        for i in range((lon_start+7),lon_end):
            temp=report2[i]
            
            lon=lon+temp
            
        print(lat) # test printing cases for debug 
        print(lon)
    lat=float(lat) # converts from the sting for concatinaion to float 
    lon=float(lon)
    return lat, lon # returns data this file is desighned to be used as a a subroutine 

