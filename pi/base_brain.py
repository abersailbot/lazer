import math
#from wind_direction_sensor import WindSensor
from tabulate import tabulate
import global_pos
import servo

def update_boom(change_angle):
    #send data to arduino to update position
    print()
    
def update_rudder(change_angle):
    print("data receved")
    print(change_angle)
    if change_angle <-5: # checks if left turn needed with 10 degree margin of error
        servo.servopos(130)
        print("left turn taken")
    elif change_angle >5:# checks if right turn needed with 10 degree margin of error
        servo.servopos(0)
        print("right turn taken")
    else:#if not within those margins keep strait
        servo.servopos(60)
        print("rudder returned to strait")


def calculate_boom_angle(wind_direction,heading): # finds semi optimal sail angle
    sail_bearing = (wind_direction + heading) / 2
    if sail_bearing > 90:
        sail_bearing = 180 - sail_bearing
    return sail_bearing

def find_wind_direction():
    #return WindSensor.getWindDirectionAsDeg()
    # ^ not yet working
    wind_direction = int(input("enter wind direction as compass heading"))
    return wind_direction

def calculate_bearing(current_lat, current_long, waypoint_lat, waypoint_long):
    # Calculate the angle (azimuth) between the two coordinates
    delta_lat = waypoint_lat - current_lat
    delta_long = waypoint_long - current_long
    azimuth_rad = math.atan2(delta_long, delta_lat)

    # Convert radians to degrees
    azimuth_deg = math.degrees(azimuth_rad)

    # Adjust azimuth to be in the range [0, 360)
    azimuth_deg = (azimuth_deg + 360) % 360

    # Calculate the difference between north and azimuth
    turn_angle = (azimuth_deg - 0 + 360) % 360

    return turn_angle

def calculate_compass_change(current_direction, desired_direction):
    # Ensure the input values are within the valid range (0 to 360)
    current_direction = current_direction % 360
    desired_direction = desired_direction % 360

    # Calculate the change needed to face the desired direction
    compass_change = (desired_direction - current_direction + 180) % 360 - 180

    return compass_change

'''def headding_adjust(compass_change):
    print("here")
    compass_current=int(input("enter current compass headding"))
    if compass_current >= (compass_change-10) and compass_current <= (compass_change+10):#checking if it is within acceptable margins 
        print("within acceptable margins no change")
        update_rudder(int(60))#sets rudder to strait on
    elif compass_current > compass_change: # if greater turn right
        update_rudder(int(0))
    else :#if right turn not needed then left turn
        update_rudder(int(130))
old code does not work '''  

def get_gps_loc():
    lat,long=global_pos.gps_loc()
    print("lat and long are ",lat,long)
    return lat, long

def current_waypoint(waypoints_lat,waypoints_long,current_waypoint_number):
    required_proximity=5 # in m the minimum closeness you need to be from the waypoint to move to the next waypoint
    distance_from_waypoint=float(input("enter the distance from waypoint in m")) # stopgap mesure waiiting implemtation of full gps 
    try:
        if distance_from_waypoint<required_proximity:
                current_waypoint_number=current_waypoint_number+1
                print(current_waypoint_number)
                print(waypoints_lat[current_waypoint_number],waypoints_long[current_waypoint_number])
    except:
        print("arrived at final waypoint")
        exit()

    return waypoints_lat[current_waypoint_number],waypoints_long[current_waypoint_number],current_waypoint_number

#waypoint data input
print("enter the waypoints gps cordinates (lat then long) then ANY non numeric charicter to finish inputs")
waypoints_lat=[]
waypoints_long=[]
while True: # loop adds waypoints data to lists
    try:
        temp_lat=float(input("enter lat for waypoint"))
        temp_long=float(input("enter long for waypoint"))
        waypoints_lat.append(temp_lat)
        waypoints_long.append(temp_long)
    except:
        break
print(tabulate({"lat": waypoints_lat,"long": waypoints_long}, headers="keys", tablefmt='orgtbl')) # prints nicely ordered teble with waypointt data
current_waypoint_number=0


while True: # primary thought loop
    # gps stuff
    #current_lat, current_long = get_gps_loc()
    current_lat = 10
    current_long = 10
    waypoint_lat, waypoint_long , current_waypoint_number = current_waypoint(waypoints_lat,waypoints_long,current_waypoint_number)
    current_direction = float(input("enter current heading"))



    turn_angle = calculate_bearing(current_lat, current_long, waypoint_lat, waypoint_long)
    print(f"You need to take the heading {turn_angle:.2f} degrees.")
    wind_direction=find_wind_direction()
    print("The wind direction is ",wind_direction)
    print("turn angle is ",turn_angle)
    boom_angle = calculate_boom_angle(wind_direction,turn_angle)
    print("boom should be at",boom_angle)
    desired_direction=turn_angle
    change_needed = calculate_compass_change(current_direction, desired_direction)
    print(f"Change needed: {change_needed} degrees")
    update_rudder(change_needed) # updates the rudder to take new hedding
