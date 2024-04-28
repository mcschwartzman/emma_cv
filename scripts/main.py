from ball_tracker import BallTracker

if __name__ == "__main__":

    tracker = BallTracker((29, 86, 6), (64, 255, 255))

    while(True):

        tracker.get_position()

    pass