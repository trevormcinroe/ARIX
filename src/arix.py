"""
class for ARIX hexapod connection.
"""

import serial
from serial.tools import list_ports
import tflite_runtime.interpreter as tflite
import os
import numpy as np
from camera_manager import CameraManager
import time


class ARIX:

    def __init__(self, baudrate, camera=CameraManager((512, 512)), timeout=1):
        self.baudrate = baudrate
        self.camera = camera
        self.timeout = timeout

        self.mapping = {0: 'right', 1: 'left', 2: 'backwards', 3: 'forwards', 4: 'None'}
        self.model = None
        self.input_details = None
        self.output_details = None
        self.port = None
        self.serial_connection = None

        self._start_port_conn()
        self._load_model()

    def _start_port_conn(self):
        available_ports = list_ports.comports()

        for port in available_ports:
            if 'ttyAC' in port.device:
                self.port = port.device

        self.serial_connection = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)

    def send_action(self, action):
        self.serial_connection.flush()
        self.serial_connection.write((action + '\n').encode('utf-8'))

    def _load_model(self):
        self.model = tflite.Interpreter(model_path='./src/model/arix_model_final.tflite')
        self.model.resize_tensor_input(0, (1, 512, 512, 3))
        self.model.allocate_tensors()
        self.input_details = self.model.get_input_details()
        self.output_details = self.model.get_output_details()

    def _test_model(self):
        data = np.array(np.random.random((512, 512, 3)), dtype=np.float32);
        print(data.shape)
        data = np.expand_dims(data, axis=0)
        self.model.set_tensor(self.input_details[0]['index'], data)
        self.model.invoke()
        output_data = self.model.get_tensor(self.output_details[0]['index'])
        print(output_data)

    def get_image(self):
        return self.camera.take_image()

    def get_prediction(self):
        img = self.get_image()
        img = np.expand_dims(img, axis=0)
        self.model.set_tensor(self.input_details[0]['index'], img)
        self.model.invoke()
        output_data = self.model.get_tensor(self.output_details[0]['index'])
        return np.argmax(output_data)


arix = ARIX(baudrate=9600)

for _ in range(1000):
    pred = arix.get_prediction()
    arix.send_action(action=pred)
    time.sleep(8)  # How long should we wait for the ARIX to complete her action sequence?

