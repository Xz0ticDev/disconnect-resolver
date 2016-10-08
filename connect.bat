@echo off

for /f "tokens=*" %%f in (ssid.txt) do set "ssid=%%f"
for /f "tokens=*" %%f in (interface.txt) do set "interface=%%f"

netsh wlan connect name="%ssid%" ssid="%ssid%" interface=%interface%
