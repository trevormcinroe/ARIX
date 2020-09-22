import serial
from serial.tools import list_ports
import time

available_ports = serial.tools.list_ports.comports()

for port in available_ports:
    print(port)
    if 'tty' in port.device:
        port_open = port.device

serial_con = serial.Serial(port=port_open,
                           baudrate=9600,
                           timeout=1)

print(serial_con)