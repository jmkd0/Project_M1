import random
import sys
from threading import Thread
import time

class Afficheur(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""
    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i< 5:
            for lettre in self.mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60)/100
                time.sleep(attente)
            i += 1

if __name__ == "__main__":
    #Creation des threads
    thread_1 = Afficheur("canard")
    thread_2 = Afficheur("TORTUE")

    #Lancement des threads
    thread_1.start()
    thread_2.start()

    #Attente que les threads se terminent
    thread_1.join()
    thread_2.join()

