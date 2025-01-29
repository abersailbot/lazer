import gps 
session=gps.gps(mode=gps.WATCH_ENABLE)
for i in range(1,10):
    report=session.next()
    report2=str(report)
    print(report2[10])
    print(report)
    print(report2.index("lat")
#    if report['class'] == 'SKY':
#        NSAT=0
#        for SAT in report['satellites']:
#            if SAT['used'] == True:
#                NSAT=+1
#            print("number of satallites used =",NSAT)
