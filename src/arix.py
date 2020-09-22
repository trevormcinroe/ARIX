"""

"""

import serial
from serial.tools import list_ports


class ARIX:

    def __init__(self, baudrate, timeout=1):
        self.baudrate = baudrate
        self.timeout = timeout

        self.port = None
        self.serial_connection = None

        self._start_port_conn()

    def _start_port_conn(self):
        available_ports = list_ports.comports()

        for port in available_ports:
            if 'tty' in port.device:
                self.port = port.device

        self.serial_connection = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)

    def send_action(self, action):
        self.serial_connection.write(action + '\n').encode('utf-8')
        