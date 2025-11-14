
class Deliviery:

    def __init__(self, name, latitute, longitude, priority, weight):

        self.name = name
        self.latitute = float(latitute)
        self.longitude = float(longitude)
        self.priority = priority
        self.weight = float(weight)
    


class TransportType:
    
    def __init__(self, type):
        self.type = str(type).lower()
        self.speed = None
        self.cost = None
        self.co2 = None
    
        if self.type == "car":
            self.speed = 50
            self.cost = 4
            self.co2 = 120
        elif self.type == "bike":
            self.speed = 15
            self.cost = 0
            self.co2 = 0
        elif self.type == "walking":
            self.speed = 5
            self.cost = 0
            self.co2 = 0
        else:
            # Throw
            pass


        

