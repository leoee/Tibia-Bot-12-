import pyautogui
import pyscreenshot as ImageGrab
import numpy
import cv2
from PIL import Image

class PixelConfiguration:
  def count_pix_color(self, image, color):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    MIN = numpy.array([85, 85, 85])
    MAX = numpy.array([100, 100, 100])

    dstr = cv2.inRange(img_gray, 85, 100)
    black = cv2.countNonZero(dstr)

    return black