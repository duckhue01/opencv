import datetime 
from threading import Thread
import cv2 as cv

class FPS:
    def __init__(self) -> None:
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def elapsed(self):
        return (self._end  - self._start).total_second()

    def fps(self):
        return self._numFrames / self.elapsed()


class WebcamVideoStream:
    def __init__(self, src = 0):
        self.stream = cv.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False

    def start(self):
        Thread(target=self.update)