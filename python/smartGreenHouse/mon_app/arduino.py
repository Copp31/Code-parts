# Module de lecture/ecriture du port série
# https://pyserial.readthedocs.io/en/latest/shortintro.html
# pip install pyserial
from serial import *
from threading import Thread

"""
python -m serial.tools.list_ports will print a list of available ports. 
It is also possible to add a regexp as first argument and 
the list will only include entries that matched.
"""

class Arduino:
    """Un client pour envoyer et recevoir des messages entre le Arduino et son hôte par communication série"""

    def __init__(self, port:str):
        self.port_serie = Serial(port, baudrate=9600, timeout=1, writeTimeout=1)
        self.port = port
        self.commande = []
        self.state = None
        self.data = None
        self.running = False
        self.ready = False
        self._lecture()

    def run(self):
        """ Roule un thread qui fait la lecture et l'envoie des messages en continue"""
        self.thread = Thread(target=self._main)
        self.thread.start()

    def _main(self):
        """ Lecture et l'envoie des messages en continue"""
        self.running = True
        while self.running or self.commande:
            if self.commande:
                self._ecriture()
            self._lecture()
        self.port_serie.close()

    def _lecture(self):
        """ Lecture des messages en continue, utilisé par _main"""
        if self.port_serie.isOpen():
            captured = None
            attempts = 10

            while not captured and attempts > 0:
                attempts -= 1
                ligne = self.port_serie.readline().strip()
                # print(ligne)

                try:
                    ligne2 = ligne.decode("utf-8").strip()
                    ligne2 = eval(ligne2)
                    assert type(ligne2) is dict
                    captured = ligne2
                    self.state = captured
                    self._convert_data()

                except:
                    if ligne.startswith(b"Setup"):
                        self.ready = True
                        # print(ligne)
                    # elif ligne.startswith(b"Saisie"):
                        # print(ligne)
                    # elif attempts <= 3:
                        # print(ligne)
                    else:
                        pass

    def _ecriture(self):
        """ Écriture des messages en continue, utilisé par _main"""
        if self.port_serie.isOpen() and self.ready:
            commande = " ".join(self.commande)+" "
            self.commande = []
            print("write:", commande.strip())
            self.port_serie.write(commande.encode())


    def _convert_data(self):
        data = {}
        data["humidite"] = [100-int(value*0.1466) for value in self.state["sensors"][:4]]
        data["temperature"] =  (self.state["sensors"][4] - 500) / 10
        data["pompes"] = [value for value in self.state["pompes"]]
        # print(data)
        self.data = data

    def set_cmd(self, cmd):
        """ Ajouter une commande pour l'envoie continue"""
        self.commande.append(str(cmd))

    def stop(self):
        """ Terminer le thread qui fait la lecture et l'envoie des messages en continue"""
        self.set_cmd(5)
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    import random
    import time
    print("TEST 1 - Lecture continue, ajout de commandes")
    # arduino = Arduino("/dev/ttyACM0")
    arduino = Arduino("COM3")
    arduino.run()
    time.sleep(4)
    iterations = 20
    while iterations >0:
        iterations-=1
        time.sleep(.5)
        rand = random.randint(1, 4)
        print("random:", rand)
        arduino.set_cmd(rand)

    time.sleep(3)
    arduino._convert_data()
    print("STOP!")
    arduino.stop()
    print("TEST 1 TERMINÉ")



    # print("TEST 2 - Lecture et Écriture sur demande")
    # arduino = Arduino("COM3")
    # for i in range(1,6):
    #     print(i)
    #     arduino.write(i)
    #     print(arduino.state)
    #     time.sleep(1)
    #
    # #
    # # for i in range(5):
    # #     arduino.read()
    #
    # print("TEST 2 TERMINÉ")


