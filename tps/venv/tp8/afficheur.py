import random
import sys
from threading import Thread
import time


class Afficheur(Thread):
    """Ce thread permet juste d'afficher une lettre dans la console"""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Cette méthode est exécuté lorsque le thread est en train de s'executer"""
        i = 0
        while i < 200:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1

