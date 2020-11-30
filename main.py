from src.arix import ARIX
import time

arix = ARIX(baudrate=9600)


while True:
    pred = arix.get_prediction()
    arix.send_action(action=pred)
    time.sleep(2)
