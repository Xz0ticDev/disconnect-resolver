import os
import platform
import time
from subprocess import Popen





#method determines if ping is returned
def ping(host):
    #determine ping command based on operating system
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    #return ping true or false
    print (str)(os.system("ping " + ping_str + " " + host) == 0)
    return os.system("ping " + ping_str + " " + host) == 0

def resolve():
    if(ping("google.com") == False):
        disconnectBat = Popen('disconnect.bat', cwd=r"C:\Users\PC Master Race\Desktop\disconnect_resolver")
        time.sleep(2)
        connectBat = Popen('connect.bat', cwd=r"C:\Users\PC Master Race\Desktop\disconnect_resolver")

while(True):
    resolve()
    time.sleep(1)