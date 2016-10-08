import os
import platform
import time
from subprocess import Popen

pingServer = "8.8.8.8"

#method determines if ping is returned
def ping(host):
    #determine ping command based on operating system
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    #return ping true or false
    print (str)(os.system("ping " + ping_str + " " + host) == 0)
    return os.system("ping " + ping_str + " " + host) == 0

def resolve():
    if(ping(pingServer) == False):
        disconnectBat = Popen('disconnect.bat', cwd=os.getcwd())
        time.sleep(2)
        connectBat = Popen('connect.bat', cwd=os.getcwd())
        time.sleep(2)

while(True):
    resolve()
    time.sleep(1)

exit()
