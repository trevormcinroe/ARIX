from src.arix import ARIX
import time

arix = ARIX(baudrate=9600)

print(arix.serial_connection)

for _ in range(10):
    time.sleep(3)
    arix.send_action(action='f')

    time.sleep(1)
    arix.send_action(action='b')

    time.sleep(1)
    arix.send_action(action='l')

    time.sleep(1)
    arix.send_action(action='r')
