from deliveryModels import Delivery
from validators import checkIfValid
import csv, os, logging

def loadDeliveries():

    validDeliveries = []

    # Filespaths to the files
    patternPath = os.path.join(os.path.dirname(__file__),"data","deliveries.csv")
    invalidPatternPath = os.path.join(os.path.dirname(__file__),"data","rejected.csv")

    # Opens and reads the file then load the objects
    with open(patternPath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        # Writes in case there are rows with invalid inputs
        with open(invalidPatternPath,"w",newline='',encoding='utf-8') as invalid:
            # Writes the header
            write = csv.DictWriter(invalid, fieldnames=reader.fieldnames)
            write.writeheader()

            # Goes through each row adds if it does not violate checkValid class
            for row in reader:
                if checkIfValid(row):
                    delivery = Delivery(
                        row["customer"], 
                        float(row["latitude"]),
                        float(row["longitude"]),
                        row["priority"],
                        float(row["weight"]))
                    validDeliveries.append(delivery)
                else:

                    # Logs the rejected row and writes the row to rejected file
                    logging.warning("Rejected row: %r", row)
                    write.writerow(row)

    return validDeliveries


