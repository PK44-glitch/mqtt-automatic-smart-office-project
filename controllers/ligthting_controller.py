# controllers/lighting_controller.py

from devices.light_device import turn_on, turn_off

light_level = None
motion_detected = None


def process_data(sensor_type, value):
    global light_level, motion_detected

    if sensor_type == "light":
        light_level = value

    elif sensor_type == "motion":
        motion_detected = value

    handle_light()


def handle_light():
    if light_level is None or motion_detected is None:
        return

    if light_level < 300 and motion_detected:
        turn_on()
    else:
        turn_off()
        #we have decided to not code in central controller toi test coide as it will be messy
        #by keeping the code in seperate files logic stays in one place and central controller stays simple.