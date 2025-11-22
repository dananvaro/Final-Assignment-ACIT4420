from deliveryModels import Delivery
import csv, os

def writeToFile():

    validDeliveries = []

    patternPath = os.path.join(os.path.dirname(__file__),"deliveries.csv")
    with open(patternPath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(row["customer"])


writeToFile()