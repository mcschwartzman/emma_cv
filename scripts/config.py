# time limit on evaluation in seconds, increase if we want to spend more time on each genome
evaluation_s = 1

# penalty added to the error running average if the we drop ball, increase if you want dropping genomes to be ranked lower
drop_penalty = 50

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
            "y": 220
        },
        "lower_right": {
            "x": 400,
            "y": 300
        },
        "center": {
            "x": 310,
            "y": 260
        }
    }
}
