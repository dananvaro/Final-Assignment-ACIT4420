import math

def calculateHaversine(latOne,lonOne,latTwo,lonTwo):

    # Expection/warning

    # Earths radius 
    r = 6371

    # Convert to radians
    latOne = math.radians(latOne)
    lonOne = math.radians(lonOne)
    latTwo = math.radians(latTwo)
    lonTwo = math.radians(lonTwo)

    # Difference in Latitude and Longitude
    dLat = latTwo - latOne
    dLon = lonTwo - lonOne
    
    # Central angle between two points
    a = (math.sin(((dLat/2)))**2) + math.cos(latOne)*math.cos(latTwo)*(math.sin((dLon/2))**2)

    # Central angle
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    # Distance 
    d = r * c


    return round(d,2)