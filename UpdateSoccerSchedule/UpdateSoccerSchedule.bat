@echo off
setlocal

set SCRIPT=%~dp0UpdateSoccerSchedule.py
set PYTHON=C:\Python36\python.exe

echo %PYTHON% %SCRIPT% 2021Spring_14U_Division1
%PYTHON% %SCRIPT% 2021Spring_14U_Division1 >UpdateSoccerSchedule.log