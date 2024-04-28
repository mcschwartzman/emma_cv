from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# based heavily on https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

lower_color = ()
upper_color = ()
points = deque(maxlen=32)

stream = VideoStream(src=0).start()
