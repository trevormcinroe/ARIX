import serial
from serial.tools import list_ports
import time

available_ports = serial.tools.list_ports.comports()

for port in available_ports:
    print(port)
    if 'usb' in port.device:
        port_open = port.device

