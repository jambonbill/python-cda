#https://ww2.ac-poitiers.fr/sc_phys/sites/sc_phys/IMG/pdf/programmer_carte_arduino_langage_python.pdf
from pyfirmata import Arduino, util
import time

carte = Arduino('COM8')
acquisition = util.Iterator(carte)
acquisition.start()

sortie = carte.get_pin('d:10:o') # voie 10 en sortie digitale

time.sleep(1.0) # temps d'initialisation de la carte

sortie.write(True) # envoie 5V sur la sortie

time.sleep(4) # attendre 4 secondes

sortie.write(False) # mettre la sortie à 0V

carte.exit()

