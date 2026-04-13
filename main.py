import threading 
from controllers.ligthting_controller import run_controller as run_ligthing 
from controllers.security_controller import run_controller as run_security 

light_thread = threading.Thread(target=run_ligthing)
security_thread = threading.Thread(target=run_security)

light_thread.start()
security_thread.start()

light_thread.join()
security_thread.join()