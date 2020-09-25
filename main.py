from src.arix import ARIX
import time

arix = ARIX(baudrate=9600)

action_mapping = {
    0: 'NA',
    1: 'f',
    2: 'b',
    3: 'r',
    4: 'l'
}


while True:
    # Here, an image would be taken with the camera on the Pi
    # Then, the image would be pre-processed and then fed into the NN
    # Out of the NN comes a predictions
    # Finally, the prediction is transformed into an action and sent to the robot
    time.sleep(3)
    arix.send_action(action='f')

    time.sleep(1)
    arix.send_action(action='b')

    time.sleep(1)
    arix.send_action(action='l')

    time.sleep(1)
    arix.send_action(action='r')
