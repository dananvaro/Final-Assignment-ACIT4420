import logging, sys, warnings

from io_handler import loadDeliveries, writeRoutes
from optimizer import optimizer

from deliveryModels import Delivery, TransportType



# Pythons logging function
logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s] %(message)s"
)

# Warning format
warnings.simplefilter("always")
warnings.formatwarning = lambda message, category, filename, lineno, file: f"{category.__name__}: {message}\n"

# Simple formatter that formats to hours and minutes
def formatToHours(time):
    hours = int(time)
    minutes = int((time-hours) * 60)

    return f"{hours}h {minutes}m"

def main():

    logging.info("-------------------- Start of optimiztion --------------------")

    # Loads deliveries from file
    listOfDeliveries = loadDeliveries()

    # Checks if there are more than two deliveries.
    if len(listOfDeliveries) <= 2:
        print("Not enought deliveries, please update deliveries.")
        logging.warning("Not enough deliveries")
        sys.exit(1)


    # Gets the depot
    depot = listOfDeliveries[0]
    
    # Asks the user the transport type and optimization
    while True: 

        try: 

            userInput = int(input("Select transport mode: \n 1. Car \n 2. Bicycle \n 3. Walking \n"))

            if(userInput == 1):
                transport = TransportType("Car")
                break
            elif(userInput == 2):
                transport = TransportType("Bike")
                break
            elif(userInput == 3):
                transport = TransportType("Walking")
                break
            else: 
                warnings.warn("That's a invalid options, pick 1, 2, or 3")
                continue


        except (ValueError, TypeError) as e: 
            warnings.warn("That's a invalid options, pick 1, 2, or 3")


    while True: 

        try: 

            userInput = int(input("Select optimization mode: \n 1. Fastest time \n 2. Lowest cost \n 3. Lowest CO2 \n"))

            if(userInput == 1):
                criteria = "fastest"
                break
            elif(userInput == 2):
                criteria = "cheapest"
                break
            elif(userInput == 3):
                criteria = "lowest"
                break
            else: 
                warnings.warn("That's a invalid options, pick 1, 2, or 3")
                continue

        except (ValueError, TypeError) as e: 
            warnings.warn("That's a invalid options, pick 1, 2, or 3")

    # Logs the metrics
    logging.info(f"Selected transport mode: {transport.type}")
    logging.info(f"Selected optimization mode: {criteria}")
    logging.info(f"Depot location {depot.latitude} and {depot.longitude}")
    logging.info(f"Numbers of deliveries: {len(listOfDeliveries)-2}")
    
    ((routes, metrics), startTime, endTime) = optimizer(listOfDeliveries, depot, transport,criteria)

    logging.info(f"Totals for routes: Total distance: {metrics['totalDistance']:.3f} km, total time: {formatToHours(metrics['totalTime'])}," + 
                 f"total cost: {metrics['totalCost']:.2f} kr, total CO2: {metrics['totalCO2']:.2f} g")
    logging.info("-------------------- End of optimiztion --------------------")

    # Writes the route to a file
    writeRoutes(routes)

    print("--- Summary ---")
    print(f"Transport type: {transport.type.capitalize()}")
    print(f"Optimization method: {criteria.capitalize()}\n")
    print(f"Total distance: {metrics['totalDistance']:.3f} km")
    print(f"Total time: {formatToHours(metrics['totalTime'])}")
    print(f"Total cost: {metrics['totalCost']:.2f} kr")
    print(f"Total CO2: {metrics['totalCO2']:.2f} g \n")
    print(f"Execution time: {(endTime-startTime)* 1000:.3f} ms")

if __name__ == "__main__":

    main()