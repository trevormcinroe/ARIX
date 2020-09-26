"""

"""

import time
import os
from picamera import PiCamera


class CameraManager:
    """
    Attributes:
        resolution (tuple of ints): <wxh> of video
        video_length (int): length of the videos being taken
    """

    def __init__(self, resolution, video_length):
        self.resolution = resolution
        self.video_length = video_length

        self.camera = PiCamera()
        self.camera.resolution = self.resolution

    def take_video(self, file_name):
        """A method that records a video of self.video_length seconds

        Args:
            file_name (str): filename to save the .mp4 to

        Returns:
            .mp4 file
        """
        self.camera.start_preview()

        self.camera.start_recording('./' + file_name + '.mp4')
        time.sleep(self.video_length)
        self.camera.stop_recording()
        self.camera.stop_preview()

    def take_picture(self, file_name):
        """"""
        self.camera.start_preview()
        self.camera.capture('./' + file_name + '.jpg')
        self.camera.stop_preview()
