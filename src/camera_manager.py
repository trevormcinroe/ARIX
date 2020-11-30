"""

"""

import time
import os
from io import BytesIO
from PIL import Image
from picamera import PiCamera
import numpy as np


class CameraManager:
    """
    Attributes:
        resolution (tuple of ints): <wxh> of video
        video_length (int): length of the videos being taken
    """

    def __init__(self, resolution):
        self.resolution = resolution

        self.camera = PiCamera()
        self.camera.resolution = self.resolution

    def take_video(self, file_name, video_length):
        """A method that records a video of self.video_length seconds

        Args:
            file_name (str): filename to save the .mp4 to

        Returns:
            .mp4 file
        """
        self.camera.start_preview()
        # The pi's camera is not compatible with .mp4
        self.camera.start_recording('./' + file_name + '.h264')
        time.sleep(video_length)
        self.camera.stop_recording()
        self.camera.stop_preview()

    def take_image(self):
        self.camera.start_preview()
        time.sleep(0.5)
        self.camera.capture('./test.jpg')
        image = Image.open('./test.jpg')
        self.camera.stop_preview()
        os.remove('./test.jpg')
        return np.array(image, dtype=np.float32) / 255.

    def test(self):
        self.camera.start_preview()
        self.camera.capture('./test.jpeg')
        self.camera.stop_preview()
