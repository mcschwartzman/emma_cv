# time limit on evaluation in seconds, increase if we want to spend more time on each genome
<<<<<<< HEAD
evaluation_s = 5
=======
evaluation_s = 20
>>>>>>> 7def649 (new squares)

# penalty added to the error running average if the we drop ball, increase if you want dropping genomes to be ranked lower
drop_penalty = 500

# max size of population, this should always be at least 2 more than the generation_size (otherwise you won't have enough genomes to procreate)
population_cap = 16

# max size of generation, ALSO the number of genomes to cull, so make sure this is always at least 2 less than population size
generation_size = 8

# amount of time in seconds between telemetry strings sent to arduino, should always be slightly less than the serial timeout time on the arduino
telemetry_delay = 0.1

# this is the port that my arduino shows up as on Mathew's computer! yours will likely be different!
serial_port = '/dev/cu.usbmodem1101'   

# these are simple boxes that represent the bounds of each platform, adjust boxes to capture platforms in frame
platforms = {
    "platform_a_bounds" : {
        "label": "A",
        "upper_left": {
            "x": 240,
            "y": 70
        },
        "lower_right": {
            "x": 380,
            "y": 145
        },
        "center": {
            "x": 310,
            "y": 110
        }
    },
    "platform_b_bounds" : {
        "label": "B",
        "upper_left": {
            "x": 310,
            "y": 120
        },
        "lower_right": {
            "x": 440,
            "y": 280
        },
        "center": {
            "x": 375,
            "y": 190
        }
    },
    "platform_c_bounds" : {
        "label": "C",
        "upper_left": {
            "x": 120,
            "y": 140
        },
        "lower_right": {
            "x": 300,
            "y": 290
        },
        "center": {
            "x": 221,
            "y": 205
        },
        "motors": {
            "theta_7": 93,
            "theta_8": 207,
            "theta_9": 326

        }
    }
}
