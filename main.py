import threading

from controllers.lighting_controller import run_controller as run_lighting_controller
from controllers.security_controller import run_controller as run_security_controller
from sensors.motion_sensor import run_lighting_sensor, run_security_sensor
from devices.alarm import run_alarm
from dashboard import run_dashboard


lighting_controller_thread = threading.Thread(target=run_lighting_controller)
security_controller_thread = threading.Thread(target=run_security_controller)
lighting_sensor_thread = threading.Thread(target=run_lighting_sensor)
security_sensor_thread = threading.Thread(target=run_security_sensor)
alarm_thread = threading.Thread(target=run_alarm)
dashboard_thread = threading.Thread(target=run_dashboard)

lighting_controller_thread.start()
security_controller_thread.start()
lighting_sensor_thread.start()
security_sensor_thread.start()
alarm_thread.start()
dashboard_thread.start()

lighting_controller_thread.join()
security_controller_thread.join()
lighting_sensor_thread.join()
security_sensor_thread.join()
alarm_thread.join()
dashboard_thread.join()