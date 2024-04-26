from gpiozero import Motor
from time import sleep

# Définition des moteurs
motor_left = Motor(forward=17, backward=18)   # Pins pour le moteur gauche
motor_right = Motor(forward=27, backward=22)  # Pins pour le moteur droit

def move_forward(duration):
    """ Fonction pour faire avancer le robot """
    motor_left.forward()  # Démarre le moteur gauche en avant
    motor_right.forward() # Démarre le moteur droit en avant
    sleep(duration)       # Continue d'avancer pendant 'duration' secondes
    motor_left.stop()     # Arrête le moteur gauche
    motor_right.stop()    # Arrête le moteur droit

# Test de la fonction

# move_forward(5)  # Fait avancer le robot pendant 5 secondes

def move_backward(duration):
    """ Fonction pour faire reculer le robot """
    motor_left.backward()  # Démarre le moteur gauche en arrière
    motor_right.backward() # Démarre le moteur droit en arrière
    sleep(duration)        # Continue de reculer pendant 'duration' secondes
    motor_left.stop()      # Arrête le moteur gauche
    motor_right.stop()     # Arrête le moteur droit

# Test de la fonction
# move_backward(5)  # Fait reculer le robot pendant 5 secondes

def turn_right(duration):
    """ Fonction pour faire tourner le robot à droite """
    motor_left.forward()   # Démarre le moteur gauche en avant pour pivoter
    motor_right.backward() # Démarre le moteur droit en arrière pour aider au pivot
    sleep(duration)        # Continue de tourner pendant 'duration' secondes
    motor_left.stop()      # Arrête le moteur gauche
    motor_right.stop()     # Arrête le moteur droit

# Test de la fonction
# turn_right(2)  # Fait tourner le robot à droite pendant 2 secondes

def turn_left(duration):
    """ Fonction pour faire tourner le robot à gauche """
    motor_left.backward()  # Démarre le moteur gauche en arrière pour aider au pivot
    motor_right.forward()  # Démarre le moteur droit en avant pour pivoter
    sleep(duration)        # Continue de tourner pendant 'duration' secondes
    motor_left.stop()      # Arrête le moteur gauche
    motor_right.stop()     # Arrête le moteur droit

# Test de la fonction
#turn_left(2)   # Fait tourner le robot à gauche pendant 2 secondes
