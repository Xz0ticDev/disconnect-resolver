import os

os.remove("interface.txt")

tmp = os.popen("netsh wlan show profile").read()

interface = tmp[23:(tmp.index(":"))]

file = open("interface.txt", "w")

file.write(interface)

file.close()