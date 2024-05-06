#here we are tracking ball
from ball_tracker import BallTracker

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

        print(ball_position)

        tracker.show_frame()

        