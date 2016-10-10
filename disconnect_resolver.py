import os
import time
import winsound
from subprocess import Popen

#server to test ping
pingServer = "8.8.8.8"

#call batch file to disconnect from internet
def disconnect():
    Popen('disconnect.bat', cwd=os.getcwd())
    winsound.PlaySound(os.getcwd() + "\disconnected.wav", winsound.SND_FILENAME)

#call batch file to connect to internet
def connect():
    Popen('connect.bat', cwd=os.getcwd())
    winsound.PlaySound(os.getcwd() + "\connected.wav", winsound.SND_FILENAME)

#detects connection errors
def ping(host):

    #return ping true or false
    print (str)(os.system("ping -n 1 " + host) == 0)
    return os.system("ping -n 1 " + host) == 0

#disconnect and reconnect to internet if  connection error was detected
def resolve():
    if(ping(pingServer) == False or getRawPing() > 100):
        disconnect()
        time.sleep(2)
        connect()
        time.sleep(2)

def getRawPing():
    ping = os.popen('ping ' + pingServer + ' -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    ms = msLine[len(msLine) - 4:len(msLine) - 2]
    print ms
    return int(ms)

#loop program with 2 second interval
while(True):
    resolve()
    time.sleep(2)

#exit program
exit()
