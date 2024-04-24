def gps_loc():
    import gps
    session=gps.gps(mode=gps.WATCH_ENABLE)
    lat=""
    lon=""
    for i in range(1,10):
        report=session.next()
        report2=str(report)
        print(report2[10])
        print(report)
        lat_start=0
        lat_end=0
        lat=""
        lon_start=0
        lon_end=0
        lon=""
        try:
            lat_start=report2.index("'lat': ")
            print("found")
            lat_end=report2.find(",",lat_start)
            print(lat_start,"to",lat_end)
        except:
            print("not found")
        for i in range((lat_start+7),lat_end):
            temp=report2[i]
            
            lat=lat+temp
            
        try:
            lon_start=report2.index("'lon': ")
            print("found")
            lon_end=report2.find(",",lon_start)
            print(lon_start,"to",lon_end)
        except:
            print("not found")
        for i in range((lon_start+7),lon_end):
            temp=report2[i]
            
            lon=lon+temp
            
        print(lat)
        print(lon)
    lat=float(lat)
    lon=float(lon)
    return lat, lon

