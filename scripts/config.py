# time limit on evaluation in seconds, increase if we want to spend more time on each genome
evaluation_s = 5

# penalty added to the error running average if the we drop ball, increase if you want dropping genomes to be ranked lower
drop_penalty = 50

# max size of population, this should always be at least 2 more than the generation_size (otherwise you won't have enough genomes to procreate)
population_cap = 16

# max size of generation, ALSO the number of genomes to cull, so make sure this is always at least 2 less than population size
generation_size = 8

# amount of time in seconds between telemetry strings sent to arduino, should always be slightly less than the serial timeout time on the arduino
telemetry_delay = 0.1

# this is the port that my arduino shows up as on Mathew's computer! yours will likely be different!
serial_port = '/dev/cu.usbmodemF412FA6F2F702'   

# these are simple boxes that represent the bounds of each platform, adjust boxes to capture platforms in frame
platforms = {
    "platform_a_bounds" : {
        "label": "A",
        "upper_left": {
            "x": 80,
            "y": 30
        },
        "lower_right": {
            "x": 200,
            "y": 150
        },
        "center": {
            "x": 140,
            "y": 90
        }
    },
    "platform_b_bounds" : {
        "label": "B",
        "upper_left": {
            "x": 320,
            "y": 40
        },
        "lower_right": {
            "x": 480,
            "y": 160
        },
        "center": {
            "x": 400,
            "y": 100
        }
    },
    "platform_c_bounds" : {
        "label": "C",
        "upper_left": {
            "x": 220,
            "y": 180
        },
        "lower_right": {
            "x": 400,
            "y": 300
        },
        "center": {
            "x": 310,
            "y": 260
        },
        "motors": {
            "theta_7": 93,
            "theta_8": 207,
            "theta_9": 326
        }
    }
}
