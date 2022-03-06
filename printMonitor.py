import mss
import cv2
import numpy as np
from time import sleep

def printMonitor():
    with mss.mss() as sct:
        escolherMonitor = 1
        mon = sct.monitors[escolherMonitor]
        monitor = {
            "top": mon["top"],
            "left": mon["left"],
            "width": mon["width"],
            "height": mon["height"],
            "mon": escolherMonitor,
        }
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        cv2.imwrite('./images/image.png',img)
        sleep(0.5)