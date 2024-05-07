#here we are tracking ball
from ball_tracker import BallTracker
from config import frame_center

from serial import Serial
from time import sleep


port = '/dev/cu.usbmodemF412FA6F2F702'  # this is the port that my arduino shows up as on my computer! yours will likely be different!
connection = Serial(port, 115200)   

if __name__ == "__main__":

    # experimental values
    yellow_lower = (255, 135, 0)
    yellow_upper = (255, 255, 50)
    dark_green_lower = (7, 66, 16)

    # RGB values from tutorial goes from lightest to darkest and can tweak to be very specific to ball but the narrower make it the more specific the settings like lighting have to be
    green_lower = (29, 86, 6)
    green_upper = (64, 255, 255)

    #green_lower = (2, 41, 12)
    #green_upper = (10, 245, 70)
    #green_upper = (7, 255, 42)
    #green_lower = (9, 61, 22)
    #green_lower = (17, 74, 32)
    #green_lower = (29, 86, 6) DARKEST
    #green_upper = (64, 255, 255) LIGHTEST

    tracker = BallTracker(green_lower, green_upper)

    while(True):

        ball_position = tracker.get_position()



        if(ball_position):

            x = int(ball_position[0])
            y = int(ball_position[1])

            message = "TEL{}x{}y".format(x, y)

            print("sending '{}'".format(message))

            connection.write(message.encode('utf-8'))


            if connection.in_waiting > 0:

                response = connection.readline()

                print(response.decode())


        tracker.show_frame()

        
def xy_to_rtheta(x, y):

    # the origin is the upper left of the frame

    return (r, theta)