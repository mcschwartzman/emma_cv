#here we are tracking ball
from ball_tracker import BallTracker
from config import frame_center, serial_port, evaluation_s, drop_penalty
from genetic_algorithm import GeneticAlgorithm

from serial import Serial
from time import sleep, time

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




if __name__ == "__main__":

    total_generations = 0

    sga = GeneticAlgorithm(population_cap=16, generation_size=8)
    sga.initialize_population()

    tracker = BallTracker(green_lower, green_upper)

    while(True):

        total_generations += 1
        print("{} total generations".format(total_generations))

        # Step 1: define population

        # Step 2: loop until ball disappears, or until out of time

        for genome in sga.get_unevaluated():

            # send new PID values to arduino
            message = "PID{0}p{1}i{2}d".format(genome.chromosome['p_gain'], genome.chromosome['i_gain'], genome.chromosome['d_gain'])
            print(message)

            connection.write(message.encode('utf-8'))

            ball_tracked = tracker.get_r_theta()
            while(not ball_tracked):
                print("waiting for ball")
                ball_tracked = tracker.get_r_theta()
                tracker.show_frame()

            start_time = time()
            evaluating = True
            r_sum = 0
            r_count = 0

            while(evaluating):

                ball_tracked = tracker.get_r_theta()
                tracker.show_frame()
                current_time = time()

                if(ball_tracked):

                    r, theta, platform = ball_tracked
                    message = "TEL{}r{}theta{}table".format(int(r), int(theta), platform['label'])
                    # print("sending '{}'".format(message))
                    connection.write(message.encode('utf-8'))

                    r_sum += r
                    r_count += 1

                else:
                    evaluating = False
                    r_sum += drop_penalty

                if ((current_time - start_time) >= evaluation_s):
                    evaluating = False

            if not r_count:
                r_count = 1

            r_average = r_sum / r_count

            print(r_average)

            # sleep(1)
            sga.evaluate(genome, r_average)
        
        sga.clear_unevaluated()
        sga.sort_population()
        sga.cull_population()


        print("producing new generation")
        
        sga.new_generation()

        sleep(2)


        
