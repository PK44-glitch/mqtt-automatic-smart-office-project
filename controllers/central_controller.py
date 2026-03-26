from controllers.lighting_controller import handle_light

light_level = 1000
motion_detected = False

def process_message(topic, payload):
    global light_level, motion_detected

    if topic == "office/light_level":
        light_level = int(payload)

    elif topic == "office/motion":
        motion_detected = payload == "1"

    handle_light(light_level, motion_detected)