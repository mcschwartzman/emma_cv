#here we are tracking ball
from ball_tracker import BallTracker
from config import serial_port, evaluation_s, drop_penalty
from genetic_algorithm import GeneticAlgorithm

from serial import Serial
from time import sleep, time

connection = Serial(serial_port, 115200)   

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

    # define a random set of 
    sga = GeneticAlgorithm(population_cap=16, generation_size=8)
    sga.initialize_population()

    # initialize ball tracker
    tracker = BallTracker(green_lower, green_upper)
    sleep(1)

    while(True):

        total_generations += 1
        print("{} total generations".format(total_generations))

        # for every genome that needs to be evaluated
        for genome in sga.get_unevaluated():

            # send new PID values to arduino
            pid_message = "PID{:.4f}p{:.4f}i{:.4f}d\n".format(genome.chromosome['p_gain'], genome.chromosome['i_gain'], genome.chromosome['d_gain'])
            print(pid_message)

            connection.write(pid_message.encode('utf-8'))
            

            # while (connection.in_waiting < 3):
            #     sleep(0.025)
            
            # if(connection.in_waiting > 0):
            #     print("data available!")
            #     arduino_response = connection.readline()
            #     print(arduino_response)
            

            # Wait for the ball to come into view, so that we don't just automatically fail a genome

            ball_tracked = tracker.get_r_theta()
            while(not ball_tracked):
                # print("waiting for ball")
                ball_tracked = tracker.get_r_theta()
                tracker.show_frame()

            # Start the clock to evaluate!
            start_time = time()
            evaluating = True
            r_sum = 0
            r_count = 0

            # loop until we're done evaluating a genome
            while(evaluating):

                ball_tracked = tracker.get_r_theta()
                tracker.show_frame()
                current_time = time()

                # as long as we see the ball...
                if(ball_tracked):

                    # sleep(0.1)

                    r, theta, platform = ball_tracked
                    message = "TEL{}r{:.1f}theta{}table".format(int(r), int(theta), platform['label'])
                    print("sending '{}'".format(message))
                    connection.write(message.encode('utf-8'))
                    sleep(0.1)

                    # while (connection.in_waiting < 3):
                    #     sleep(0.025)

                    if(connection.in_waiting > 0):
                        arduino_response = connection.readline()
                        print("response: ", arduino_response)

                    r_sum += r
                    r_count += 1
                
                # ...otherwise we dropped, so add the penalty and stop evaluating this genome
                else:
                    evaluating = False
                    r_sum += drop_penalty

                # check if we haven't run out the clock on this evaluation
                if ((current_time - start_time) >= evaluation_s):
                    evaluating = False

            # safety check in case we DID fail a genome instantly (r_cound would be 0)
            if not r_count:
                r_count = 1

            # calculate the average radius (error) which is used as the genetic algorithm fitness metric
            r_average = r_sum / r_count

            print(r_average)

            # sleep(1)
            sga.evaluate(genome, r_average)
        
        sga.clear_unevaluated()
        sga.sort_population()
        sga.cull_population()


        print("producing new generation")
        
        sga.new_generation()

        # sleep(2)


        
