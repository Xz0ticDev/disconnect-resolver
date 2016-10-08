import os
import time
from subprocess import Popen

#server to test ping
pingServer = "8.8.8.8"

#call batch file to disconnect from internet
def disconnect():
    Popen('disconnect.bat', cwd=os.getcwd())

#call batch file to connect to internet
def connect():
    Popen('connect.bat', cwd=os.getcwd())

#detects connection errors
def ping(host):

    #return ping true or false
    print (str)(os.system("ping -n 1 " + host) == 0)
    return os.system("ping -n 1 " + host) == 0

#disconnect and reconnect to internet if  connection error was detected
def resolve():
    if(ping(pingServer) == False):
        disconnect()
        time.sleep(2)
        connect()
        time.sleep(2)

#loop program with 1 second interval
while(True):
    resolve()
    time.sleep(1)

#exit program
exit()
