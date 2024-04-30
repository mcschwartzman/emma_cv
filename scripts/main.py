from ball_tracker import BallTracker

if __name__ == "__main__":


    # experimental values
    yellow_lower = (255, 135, 0)
    yellow_upper = (255, 255, 50)
    dark_green_lower = (7, 66, 16)

    # values from tutorial
    green_lower = (29, 86, 6)
    green_upper = (64, 255, 255)

    tracker = BallTracker(green_lower, green_upper)

    while(True):

        ball_position = tracker.get_position()

        print(ball_position)

        tracker.show_frame()