import numpy as np
import cv2 as cv


def color_transfer(source, target):
    """
    docstring
    """
    sour = cv.cvtColor(sour, cv.COLOR_BGR2LAB).astype("float32")
    targ = cv.cvtColor(targ, cv.COLOR_BGR2LAB).astype("float32")

    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(sour)

	(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(targ)
