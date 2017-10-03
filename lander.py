import math

altitude = 1000.00
velocity = 40
fuel = 25
strength = 4
gravity = 1.622
velocity_change_per_thrust = 4

def get_status():
    global altitude
    global velocity
    global fuel
    global strength
    
    status = "Alt = {:.2f}".format(altitude) + " Vel = {:.2f}".format(velocity) + " Fuel = " + str(fuel) + " Str = " + str(strength)

    return status

def thrust(number):
    global velocity
    global fuel
    global strength
    global velocity_change_per_thrust
    global number
    
    number = math.floor(number)
    
    if number > strength:
        number = strength
    
    if number > fuel:
        number = fuel
        
    velocity -= number * velocity_change_per_thrust
    fuel -= math.floor(number)
    
    
def update_onesecond():
    global velocity
    global gravity
    global altitude
    
    velocity += gravity
    altitude -= velocity
    
    if altitude < 0:
        altitude = 0
        
def has_crashed():
    global altitude
    global velocity
    global strength
    if altitude <= 0 and velocity > strength:
        return True
    else:
        return False    
    
def has_safely_landed():
    global altitude
    global velocity
    global strength
    if altitude <= 0 and velocity <= strength:
        return True
    else:
        return False
  

#Part II

def reset_lander(a, v, f):
    global altitude
    global velocity
    global fuel
    altitude = a
    velocity = v
    fuel = f
    
def human_controller():
    get_status
    number=input("How much thrust would you like this round?")
    while number != string:
        number=input("Please enter a number of thrust you would like this round")
    number = math.floor(number)
    thrust(number)
    return number