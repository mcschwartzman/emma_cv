from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

from config import platforms

# based heavily on https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

class BallTracker(object):

    def __init__(self, color_bounds_lower, color_bounds_upper):

        self.color_bounds_lower = color_bounds_lower           
        self.color_bounds_upper = color_bounds_upper

        self.points = deque(maxlen=32)

        self.stream = VideoStream(src=0).start()
        #src = 0 is for usb webcam
        #src = 1 is for built-in webcam

        self.frame = None

        time.sleep(2.0)

    def get_position(self):

        # get the most recent frame from the video feed
        self.frame = self.stream.read()
        # print(VideoStream(src=1).width_pixels)

        # resize and convert rgb values to hsv
        self.frame = imutils.resize(self.frame, width=600)
        blurred = cv2.GaussianBlur(self.frame, (11,11), 0)
        hsv_converted = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # construct a mask of colors within the lower and upper bounds of the Ball Tracker
        mask = cv2.inRange(hsv_converted, self.color_bounds_lower, self.color_bounds_upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and find the center of them
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        center = None
        radius = 0

        # only proceed if at least one contour was found

        if (len(contours) < 1):

            # print("not enough contours")

            return None

        # find the largest contour in the mask, then use it to compute minimum enclosing circle and centroid
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        moment = cv2.moments(largest_contour)
        center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] /  moment["m00"]))
        # only proceed if the radius meets a minimum size

        if radius < 10:

            # print("circle too small")

            return None

        # draw the circle and centroid on the frame, then update list of tracked points
        cv2.circle(self.frame, (int(x), int(y)), int(radius), (0,255,255), 2)
        cv2.circle(self.frame, center, 5, (0, 0, 255), -1)

        # update the points queue
        self.points.appendleft(center)

        return (x, y)

    def get_r_theta(self):

        cartesian = self.get_position()

        if not cartesian:

            return None

        x, y = cartesian[0], cartesian[1]

        platform = self.get_table(x, y, platforms)

        if not platform:

            return None

        center = platform['center']

        leg1 = x - center['x']
        leg2 = y - center['y']

        r = np.sqrt(leg1**2 + leg2**2)

        theta = np.arctan2(leg2, leg1) * 180 / np.pi

        # swap y-axis direction
        theta = theta * -1

        # converts to absolute (from positive x-axis)
        if (theta < 0):
            theta = 360 + theta

        return (r, theta, platform)

    def get_table(self, x, y, platforms):

        if x > platforms['platform_a_bounds']['upper_left']['x'] and x < platforms['platform_a_bounds']['lower_right']['x']:

            if y > platforms['platform_a_bounds']['upper_left']['y'] and y < platforms['platform_a_bounds']['lower_right']['y']:

                return platforms['platform_a_bounds']

        if x > platforms['platform_b_bounds']['upper_left']['x'] and x < platforms['platform_b_bounds']['lower_right']['x']:

            if y > platforms['platform_b_bounds']['upper_left']['y'] and y < platforms['platform_b_bounds']['lower_right']['y']:

                return platforms['platform_b_bounds']

        if x > platforms['platform_c_bounds']['upper_left']['x'] and x < platforms['platform_c_bounds']['lower_right']['x']:

            if y > platforms['platform_c_bounds']['upper_left']['y'] and y < platforms['platform_c_bounds']['lower_right']['y']:

                return platforms['platform_c_bounds']

        return 

    def show_frame(self):

        a_start_x = platforms['platform_a_bounds']['upper_left']['x']
        a_start_y = platforms['platform_a_bounds']['upper_left']['y']
        a_end_x = platforms['platform_a_bounds']['lower_right']['x']
        a_end_y = platforms['platform_a_bounds']['lower_right']['y']

        b_start_x = platforms['platform_b_bounds']['upper_left']['x']
        b_start_y = platforms['platform_b_bounds']['upper_left']['y']
        b_end_x = platforms['platform_b_bounds']['lower_right']['x']
        b_end_y = platforms['platform_b_bounds']['lower_right']['y']

        c_start_x = platforms['platform_c_bounds']['upper_left']['x']
        c_start_y = platforms['platform_c_bounds']['upper_left']['y']
        c_end_x = platforms['platform_c_bounds']['lower_right']['x']
        c_end_y = platforms['platform_c_bounds']['lower_right']['y']

        a_center_x = platforms['platform_a_bounds']['center']['x']
        a_center_y = platforms['platform_a_bounds']['center']['y']
        
        b_center_x = platforms['platform_b_bounds']['center']['x']
        b_center_y = platforms['platform_b_bounds']['center']['y']

        c_center_x = platforms['platform_c_bounds']['center']['x']
        c_center_y = platforms['platform_c_bounds']['center']['y']

        length=100

        # angle7_start = 
        # angle8
        # angle9

        line7_x = int(c_center_x + (length * np.cos(platforms['platform_c_bounds']['motors']['theta_7'] * -3.14 / 180)))
        line7_y = int(c_center_y + (length * np.sin(platforms['platform_c_bounds']['motors']['theta_7'] * -3.14 / 180)))

        line8_x = int(c_center_x + (length * np.cos(platforms['platform_c_bounds']['motors']['theta_8'] * -3.14 / 180)))
        line8_y = int(c_center_y + (length * np.sin(platforms['platform_c_bounds']['motors']['theta_8'] * -3.14 / 180)))

        line9_x = int(c_center_x + (length * np.cos(platforms['platform_c_bounds']['motors']['theta_9'] * -3.14 / 180)))
        line9_y = int(c_center_y + (length * np.sin(platforms['platform_c_bounds']['motors']['theta_9'] * -3.14 / 180)))

        cv2.line(self.frame,(c_center_x,c_center_y),(line7_x,line7_y),(0,255,0),2)
        cv2.line(self.frame,(c_center_x,c_center_y),(line8_x,line8_y),(0,255,0),2)
        cv2.line(self.frame,(c_center_x,c_center_y),(line9_x,line9_y),(0,255,0),2)

        cv2.rectangle(self.frame, (a_start_x, a_start_y), (a_end_x, a_end_y), color=(255,0,0), thickness=2)
        cv2.rectangle(self.frame, (b_start_x, b_start_y), (b_end_x, b_end_y), color=(255,0,0), thickness=2)
        cv2.rectangle(self.frame, (c_start_x, c_start_y), (c_end_x, c_end_y), color=(255,0,0), thickness=2)

        cv2.circle(self.frame, (a_center_x, a_center_y), radius=2, color=(0,0,255), thickness=-1)
        cv2.circle(self.frame, (b_center_x, b_center_y), radius=2, color=(0,0,255), thickness=-1)
        cv2.circle(self.frame, (c_center_x, c_center_y), radius=2, color=(0,0,255), thickness=-1)


        # show the frame to our screen
        cv2.imshow("Frame", self.frame)
        key = cv2.waitKey(1) & 0xFF
