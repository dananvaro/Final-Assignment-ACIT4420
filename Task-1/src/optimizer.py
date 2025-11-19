from deliveryModels import Deliviery, TransportType
from haversine import calculateHaversine

def optimizer(listOfDeliveries):







    return

# Calculate score, lower score equals better score
def scoreForFastest(delivery, distance):

    score = distance / delivery.speed 

    score = score * priorityScore(delivery.priority)

    return score

def scoreCheapest(delivery, distance):
    
    score =  distance * delivery.cost

    score = score * priorityScore(delivery.score)


    return score

def scoreGreenest(delivery, distance):

    score = distance * delivery.co2

    score = score * priorityScore(delivery.score)
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