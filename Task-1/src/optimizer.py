from deliveryModels import Delivery
from haversine import calculateHaversine
import copy

def optimizer(listOfDeliveries, depot, transportType, inputCriteria):


    # Does a shallow copy of the list with Delivery objects
    deliveriesLeft = listOfDeliveries.copy()

    # Using dic to find the correct criteria
    criteria = {

        "fastest" : scoreForFastest,
        "cheapest" : scoreForLowestCost,
        "lowest" : scoreForLowestCO2

    }

    # Getting the right criteria
    scoreFunctions = criteria[inputCriteria]

    # Assigning the current lat and long to the depot
    currentLat = depot.latitude
    currentLon = depot.longitude

    routes = []

    totalDistance = 0.0
    totalTime = 0.0
    totalCost = 0.0
    totalCO2 = 0.0


    # Looped until all Deliveries are looped through
    while deliveriesLeft:

        # Assigning a lowest score to a high number 
        # Delivery with lowest score
        lowestScore = float('inf')
        deliveryWithLowestScore = None
        distanceFromLast = 0.0

        
        # Loops through the delvieris in deliveries left
        for delivery in deliveriesLeft:

            # Calculates distance and score
            distance = calculateHaversine(currentLat,currentLon,delivery.latitude, delivery.longitude)
            score = scoreFunctions(delivery, distance,transportType)

            # If score is low the lowest score and Delivery object will be updated
            # The distance will be saved to log metrics
            if score < lowestScore:
                lowestScore = score
                deliveryWithLowestScore = delivery
                distanceFromLast = distance
            
        


        # Then updated the current Lat and Lon for next iteration
        currentLat = deliveryWithLowestScore.latitude
        currentLon = deliveryWithLowestScore.longitude

        # Remove from deliveries left
        deliveriesLeft.remove(deliveryWithLowestScore)


        ## Add depot for last stop

        metrics = {

            "totalDistance" : totalDistance,
            "totalTime" : totalTime,
            "totalCost" : totalCost,
            "totalCO2" : totalCO2

        }

    return routes, metrics







# Calculate score, lower score equals better score
def scoreForFastest(delivery, distance,transportType):

    score = distance / transportType.speed 

    score = score * priorityScore(delivery.priority)

    return score

def scoreForLowestCost(delivery, distance,transportType):
    
    score =  distance * transportType.cost

    score = score * priorityScore(delivery.priority)


    return score

def scoreForLowestCO2(delivery, distance,transportType):

    score = distance * transportType.co2

    score = score * priorityScore(delivery.priority)
    return score


def priorityScore(priority):

    priorityScore

    if(priority == "High"):

        priorityScore = 0.6

    elif (priority == "Medium"):

        priorityScore = 1

    elif (priority == "Low"):

        priorityScore= 1.2
    else:
        pass
        # Throw warning

    return priorityScore

'''




'''