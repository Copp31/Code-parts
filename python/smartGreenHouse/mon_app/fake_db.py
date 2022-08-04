from database import Database
import datetime
from random import randint
import time

db = Database("mongodb://localhost:27017/")

for i in range(3):
    date_time = datetime.datetime.now()

    arduino_state = {"pompes": (randint(0, 1),
                                randint(0, 1),
                                randint(0, 1),
                                randint(0, 1)),
                     "senseurs": (randint(500, 550),
                                  randint(500, 550),
                                  randint(500, 550),
                                  randint(500, 550),
                                  randint(150, 175),
                                  randint(5, 30))}

    pompe1 = arduino_state["pompes"][0]
    pompe2 = arduino_state["pompes"][1]
    pompe3 = arduino_state["pompes"][2]
    pompe4 = arduino_state["pompes"][3]
    humidite1 = arduino_state["senseurs"][0]
    humidite2 = arduino_state["senseurs"][1]
    humidite3 = arduino_state["senseurs"][2]
    humidite4 = arduino_state["senseurs"][3]
    temperature = arduino_state["senseurs"][4]
    reservoir = arduino_state["senseurs"][5]

    document = {"date": date_time,
                "temperature": temperature,

                "humidite1": humidite1,
                "humidite2": humidite2,
                "humidite3": humidite3,
                "humidite4": humidite4,
                "pompe1": pompe1,
                "pompe2": pompe2,
                "pompe3": pompe3,
                "pompe4": pompe4}

    db.add_data(document)

    time.sleep(1.5)

    db.read_data({},10)