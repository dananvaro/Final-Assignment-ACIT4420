from deliveryModels import Delivery
from haversine import calculateHaversine
import copy

def optimizer(listOfDeliveries, depot, transportType, inputCriteria):

    deliveriesLeft = listOfDeliveries.copy()

    criteria = {

        "fastest" : scoreForFastest,
        "cheapest" : scoreForLowestCost,
        "lowest" : scoreForLowestCO2

    }

    scoreFunctions = criteria[inputCriteria]

    currentLat = depot.latitude
    currentLon = depot.longitude

    while not deliveriesLeft:

        lowestScore = float('inf')
        deliveryWithLowestScore = None

        for delivery in listOfDeliveries:
            score = scoreFunctions(delivery, calculateHaversine(),transportType)

    





    return

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