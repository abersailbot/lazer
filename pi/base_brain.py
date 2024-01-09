import math
from tabulate import tabulate

def update_boom(change_angle):
    #send data to arduino to update position
    print()
    
def update_rudder(change_angle):
    #send data to arduino to update position
    print()
    
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

def get_gps_loc():
    #this part of the code does not exist yet so temp values are in use
    return 53.4663, -2.5942

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
    current_lat, current_long = get_gps_loc()
    waypoint_lat, waypoint_long , current_waypoint_number = current_waypoint(waypoints_lat,waypoints_long,current_waypoint_number)
    current_direction = float(input("enter current heading"))



    turn_angle = calculate_bearing(current_lat, current_long, waypoint_lat, waypoint_long)
    print(f"You need to take the heading {turn_angle:.2f} degrees.")


    desired_direction=turn_angle
    change_needed = calculate_compass_change(current_direction, desired_direction)
    print(f"Change needed: {change_needed} degrees")
    update_rudder(change_needed) # upodates the rudder to take new hedding
