import sys
import threading
import time
##local imports
sys.path.append('scripts')
import webserver

print ("DisWeb Alpha 0.1")

webthread = threading.Thread(target=webserver.run)
webthread.start()

time.sleep(0.5)

print("hello")

import disdownload
