# time limit on evaluation in seconds
evaluation_s = 5

frame_center = {
    "x": 313,
    "y": 189
}  # center of frame in pixel x, y on mathew's laptop

# these are simple boxes that represent the bounds of each platform

serial_port = '/dev/cu.usbmodemF412FA6F2F702'   
# this is the port that my arduino shows up as on my computer! yours will likely be different!

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
