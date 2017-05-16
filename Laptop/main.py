from threading import Thread
from util import coms_client
import TestApp
import io

#global variables that will be used to communicate between the coms_thread and the joy_thread and the UI_thread




#code for UI


#code for

#creation of threads and classes
# coms thread
coms_thread = Thread(target=coms_client.run_client())
io_thread = Thread(target=io.update_joystick())
# the class for the GUI
gui = TestApp()




io_thread.start()
coms_thread.start()
gui.run()

