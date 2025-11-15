import math

def calculateHaversine(latOne,lonOne,latTwo,lonTwo):
    r = 6371

    latOne = math.radians(latOne)
    lonOne = math.radians(lonOne)
    latTwo = math.radians(latTwo)
    lonTwo = math.radians(lonTwo)

    dLat = latTwo - latOne
    dLon = lonTwo - lonOne
    
    a = (math.sin(((dLat/2)))**2) + math.cos(latOne)*math.cos(latTwo)*(math.sin((dLon/2))**2)

    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))

    d = r * c


    return round(d,2)

print(calculateHaversine(35.6895,139.6917,-33.8688,151.2093))