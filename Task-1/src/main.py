import logging

from io_handler import loadDeliveries

from deliveryModels import Delivery

logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s] %(message)s"
)

listOfDeliveries = loadDeliveries()

for delivery in listOfDeliveries:
    print(delivery.name)