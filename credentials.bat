@echo off

del ssid.txt

set /p ssid=Enter Internet SSID:

echo %ssid%> ssid.txt

