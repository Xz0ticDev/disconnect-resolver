@echo off

for /f "tokens=*" %%f in (ssid.txt) do set "ssid=%%f"

netsh wlan connect name="%ssid%" ssid="%ssid%"
