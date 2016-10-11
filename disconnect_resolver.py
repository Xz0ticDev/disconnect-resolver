import os
import time
import winsound
from subprocess import Popen
from termcolor import colored, cprint

#declare variables
pingServer = "8.8.8.8"
totalPings = 0
numPings = 0

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
    return os.system('ping -n 1 ' + host + " > nul") == 0

#disconnect and reconnect to internet if  connection error was detected
def resolve():

    #checks for connection interruption
    if(ping(pingServer) == False):
        cprint("\n\nERROR: Connection interrupted.", 'red', attrs = ['bold'])
        disconnect()
        time.sleep(1)
        connect()
        time.sleep(1)

    #checks for high ping
    elif(getRawPing() > 100):
        cprint("\n\nERROR: High latency.", 'red', attrs = ['bold'])
        disconnect()
        time.sleep(1)
        connect()
        time.sleep(1)

#returns ping as integer
def getRawPing():
    global totalPings
    global numPings
    ping = os.popen('ping ' + pingServer + ' -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    ms = msLine[len(msLine) - 4:len(msLine) - 2]
    totalPings += int(ms)
    numPings += 1
    print '\r{0}'.format("Average ping: " + str(totalPings / numPings) + "ms"),
    return int(ms)

#main function
if __name__ == "__main__":

    #loop program with 2 second interval
    while(True):
        resolve()
        time.sleep(2)

#exit program
exit()
