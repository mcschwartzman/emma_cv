frame_center = {
    "x": 313,
    "y": 189
}  # center of frame in pixel x, y on mathew's laptop

# these are simple boxes that represent the bounds of each platform

serial_port = '/dev/cu.usbmodemF412FA6F2F702'   
# this is the port that my arduino shows up as on my computer! yours will likely be different!

platforms = {
    "platform_a_bounds" : {
        "upper_left": {
            "x": 80,
            "y": 30
        },
        "lower_right": {
            "x": 200,
            "y": 150
        }
    },
    "platform_b_bounds" : {
        "upper_left": {
            "x": 320,
            "y": 40
        },
        "lower_right": {
            "x": 480,
            "y": 160
        }
    },
    "platform_c_bounds" : {
        "upper_left": {
            "x": 220,
            "y": 220
        },
        "lower_right": {
            "x": 400,
            "y": 300
        }
    }
}
