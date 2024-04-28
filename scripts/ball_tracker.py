from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# based heavily on https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

class BallTracker(object):

    def __init__(self, color_bounds_lower, color_bounds_upper):

        self.color_bounds_lower = color_bounds_lower           
        self.color_bounds_upper = color_bounds_upper

        self.points = deque(maxlen=32)

        self.stream = VideoStream(src=0).start()

        time.sleep(2.0)

    def get_position(self):

        frame = self.stream.read()

        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11,11), 0)
        hsv_converted = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # construct a mask of colors within the lower and upper bounds of the Ball Tracker
        mask = cv2.inRange(hsv_converted, self.color_bounds_lower, self.color_bounds_upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and find the center of them
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        center = None

        # only proceed if at least one contour was found
        if len(contours) > 0:

            # find the largest contour in the mask, then use it to compute minimum enclosing circle and centroid
            largest_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

            moment = cv2.moments(largest_contour)
            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] /  moment["m00"]))
            # only proceed if the radius meets a minimum size

        if radius > 10:

            # draw the circle and centroid on the frame, then update list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # update the points queue
        self.points.appendleft(center)

        # show the frame to our screen
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        return
