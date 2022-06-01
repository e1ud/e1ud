#codewars 'Will you make it?' Python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump - mpg*fuel_left <= 0 else False
  
#more clever idea (not mine):
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
