#here we are tracking ball
from ball_tracker import BallTracker
from config import frame_center, platforms, serial_port
from genetic_algorithm import GeneticAlgorithm

from serial import Serial
from time import sleep

connection = Serial(serial_port)   

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


def get_table(x, y, platforms):

    if x > platforms['platform_a_bounds']['upper_left']['x'] and x < platforms['platform_a_bounds']['lower_right']['x']:

        if y > platforms['platform_a_bounds']['upper_left']['y'] and y < platforms['platform_a_bounds']['lower_right']['y']:

            return "A"

    if x > platforms['platform_b_bounds']['upper_left']['x'] and x < platforms['platform_b_bounds']['lower_right']['x']:

        if y > platforms['platform_b_bounds']['upper_left']['y'] and y < platforms['platform_b_bounds']['lower_right']['y']:

            return "B"

    if x > platforms['platform_c_bounds']['upper_left']['x'] and x < platforms['platform_c_bounds']['lower_right']['x']:

        if y > platforms['platform_c_bounds']['upper_left']['y'] and y < platforms['platform_c_bounds']['lower_right']['y']:

            return "C"

    return 

if __name__ == "__main__":

    sga = GeneticAlgorithm(population_cap=16, generation_size=8)
    sga.initialize_population()

    tracker = BallTracker(green_lower, green_upper)

    while(True):

        # need to have:
        # 1. platform bounds
        # 2. 

        # for genome in sga.unevaluated:

        #     ball_position = tracker.get_position()
        #     if(ball_position):

        #         x = int(ball_position[0])
        #         y = int(ball_position[1])

        #         message = "TEL{}r{}theta{}table".format(x, y, "1")

        #         print("sending '{}'".format(message))

        #         connection.write(message.encode('utf-8'))

        # state 2, evaluation mode:

            # for each genome in unevaluated:
                # evaluate, which means average the errors while sending telemetry to arduino

        # state 3, sort population, cull, and produce new generation

            # 

        ball_position = tracker.get_position()
        if(ball_position):

            x = int(ball_position[0])
            y = int(ball_position[1])

            platform = get_table(x, y, platforms)

            message = "TEL{}r{}theta{}table".format(x, y, platform)

            print("sending '{}'".format(message))

            connection.write(message.encode('utf-8'))


            # if connection.in_waiting > 0:

            #     response = connection.readline()

            #     print(response.decode())


        tracker.show_frame()

        
def xy_to_rtheta(x, y):



    # the origin is the upper left of the frame

    return (r, theta)